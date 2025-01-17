version: "3.8"

services:

  # Frontend ReactJS application
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - REACT_APP_BACKEND_URL=http://backend:5000  
    image: jefrey0/hello-world-frontend:latest

  # Backend Flask application
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    depends_on:
      - postgres
    environment:
      - DB_HOST=postgres
      - DB_NAME=mydatabase
      - DB_USER=user
      - DB_PASSWORD=password
    volumes:
      - ./backend:/app
    image: jefrey0/hello-world-backend:latest

  # PostgreSQL Database
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    ports:
      - "5434:5432"  # Changed to 5434
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backend/init_db.sql:/docker-entrypoint-initdb.d/init_db.sql  # Added to run the SQL initialization script

volumes:
  postgres_data:
    driver: local
