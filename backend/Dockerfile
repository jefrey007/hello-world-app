# Use the official Python image as a base
FROM python:3.9-alpine

# Install PostgreSQL development libraries to resolve pg_config issue
RUN apk update && apk add --no-cache postgresql-dev

# Install flask-cors to handle CORS issues
RUN pip install flask-cors

# Set the working directory
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies (including psycopg2-binary)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Command to run the Flask app
CMD ["python", "app.py"]
