# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set up the working directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Step 4: Copy the application code
COPY . .

# Step 5: Expose port 5000 and run the app
EXPOSE 5000
CMD ["python", "app.py"]
