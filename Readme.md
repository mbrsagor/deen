# Deen

> This application is Bangla Quran Hadith Dua and Islamic knowledge sharing platform.

## Features
- Bangla Quran Hadith Dua and Islamic knowledge sharing platform.

### Tech Stack
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Python 3.14

## Setup

```bash
# Create virtual environment
python3.14 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Docker

```bash
# Build docker image
docker build -t deen .

# Run docker container
docker run -p 8000:8000 deen
```
