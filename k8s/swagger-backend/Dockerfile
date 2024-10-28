# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set up the working directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the application code
COPY . .

# Step 5: Expose the Flask port (5000)
EXPOSE 5000

# Step 6: Run the Flask application using Gunicorn for production
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
CMD ["gunicorn", "--log-level=debug", "--access-logfile", "-", "--error-logfile", "-", "-b", "0.0.0.0:5000", "app:app"]

