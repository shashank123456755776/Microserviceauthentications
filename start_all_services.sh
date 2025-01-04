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
