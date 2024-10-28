import os
import sys
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger
from flask_cors import CORS
import logging
from flask_migrate import Migrate, upgrade
from flask.cli import with_appcontext
import click

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Configuring PostgreSQL database from environment variables
db_user = os.getenv('POSTGRES_USER', 'postgres')
db_password = os.getenv('POSTGRES_PASSWORD', 'admin')
db_host = os.getenv('POSTGRES_HOST', 'mypostgres-service')
db_port = os.getenv('POSTGRES_PORT', '5432')
db_name = os.getenv('POSTGRES_DB', 'postgres')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Swagger configuration
swagger = Swagger(app)

# Logger setup
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# CLI command to insert admin user
@click.command(name='insert_admin_user')
@with_appcontext
def insert_admin_user():
    try:
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            hashed_password = generate_password_hash('admin')
            new_user = User(username='admin', password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            logger.info("'admin' user created and committed to the database.")
        else:
            logger.info("'admin' user already exists.")
    except Exception as e:
        logger.error(f"Error inserting 'admin' user: {e}")
        db.session.rollback()

# Register the CLI command
app.cli.add_command(insert_admin_user)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Main block
if __name__ == '__main__':
    with app.app_context():
        # Run migrations
        upgrade()
        logger.info("Database migrations applied successfully.")

        # Insert admin user
        insert_admin_user()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)
