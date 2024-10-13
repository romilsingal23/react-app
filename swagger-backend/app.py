from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_cors import CORS  # Import flask-cors

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configuring PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Swagger configuration
swagger = Swagger(app)

# Example user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)



@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Parse the JSON data
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin':
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
if __name__ == '__main__':
    db.create_all()  # Ensure the database tables are created
    app.run(host='0.0.0.0', port=5000)
