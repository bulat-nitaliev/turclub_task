#!/bin/sh
# backend/entrypoint.sh

echo "⏳ Applying migrations..."
python manage.py migrate

echo "🌱 Creating sample data..."
python manage.py create_sample_data

echo "🔄 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting server..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3