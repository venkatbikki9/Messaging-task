#!/bin/bash
##This starts all 4 at a time . virtual environment, celery worker, flask, ngrok
# Activate virtual environment
source venv/bin/activate

# Start Celery worker in background
echo "Starting Celery worker..."
celery -A app.celery_app.celery_app worker --loglevel=info &

# Give Celery a few seconds to start
sleep 5

# Start Flask app
echo "Starting Flask app..."
python -m app.main &

# Give Flask a few seconds to start
sleep 5

# Start Ngrok tunnel
echo "Starting Ngrok..."
ngrok http 5000

