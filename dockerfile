# Dockerfile for a unified container hosting all microservices

# Base image for Python
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Pipfile to the container
COPY Pipfile /app/Pipfile

# Install pipenv and project dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy each microservice into the container
COPY auth_service /app/auth_service
COPY resource_service /app/resource_service
COPY task_service /app/task_service

# Expose necessary ports
EXPOSE 8000 8001 8002 8003

# Command to start the services using a script
CMD ["sh", "start_all_services.sh"]
