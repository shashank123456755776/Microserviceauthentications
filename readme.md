# Microservices Dockerized Deployment

My project contains multiple Django-based microservices deployed using Docker.

## Microservices Overview
- `auth_service`: Handles authentication and authorization.
- `resource_service`: Manages resources.
- `task_service`: Manages tasks.

## Prerequisites
1. Install Docker on my system.
2. Ensure that i  have the necessary permissions to run Docker commands in my system.

## Project Structure
```
MICROSERVICEAUTHENTICATION/
│
├── auth_service/
│   ├── manage.py              # Main Django application entry point
│   └── ...
├── resource_service/
│   ├── manage.py              # Main Django application entry point
│   └── ...
├── task_service/
│   ├── manage.py              # Main Django application entry point
│   └── ...
├── Dockerfile                 # Docker configuration file
├── start_all_services.sh      # Bash script to start all services
├── Pipfile                    # Python dependency management file
└── README.md                  # Project documentation
```

## Building the Docker Image
To build the Docker image, run:
```bash
docker build -t microservices-container .
```

## Running the Docker Container
To start the container, run:
```bash
docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 
microservices-container
```

## Accessing the Microservices
- **auth_service**: [http://localhost:8000](http://localhost:8000)
- **resource_service**: [http://localhost:8002](http://localhost:8002)
- **task_service**: [http://localhost:8001](http://localhost:8001)

## Script: `start_all_services.sh`
The `start_all_services.sh` script is executed within the Docker container to start all Django services:

```bash
#!/bin/bash

# Navigate to and start each service
cd /app/auth_service
python manage.py runserver 0.0.0.0:8000 &
echo "auth_service started on port 8000"

cd /app/resource_service
python manage.py runserver 0.0.0.0:8002 &
echo "resource_service started on port 8002"

cd /app/task_service
python manage.py runserver 0.0.0.0:8001 &
echo "task_service started on port 8001"

# Keep the container running
tail -f /dev/null
```

## Troubleshooting
### View Container Logs
Use the following command to view logs if any service fails to start:
```bash
docker logs <container_id>
```

### Stop the Container
Stop the running container with:
```bash
docker stop <container_id>
```

### Rebuild the Image
If changes are made to the services, rebuild the image:
```bash
docker build -t microservices-container .
```

# very important points .........
- Make sure to update `start_all_services.sh` if any service's port or directory changes.
- Modify the `Dockerfile` to include additional dependencies or configurations specific to your application.
