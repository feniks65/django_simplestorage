# Django SimpleStorage App

## Overview

This is a simple Django application designed to provide basic file storage functionalities. The app allows users to upload, download, and manage files.

## Features

- User authentication
- File Upload
- File Download
- File Management

## Requirements

- Python 3.9.x
- Django 4.2.16
- Django REST Framework

## Installation

### Clone the Repository

```bash
git clone https://github.com/feniks65/django_simplestorage.git
cd django_simplestorage
```

### Create a Virtual Environment

```bash
python3 -m venv env
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r ./container/requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Now, you can navigate to \`http://127.0.0.1:8000/\` in your web browser.

## API Endpoints

- \`/files/\`: File list and upload
- \`/files/<id>\`: File detail view
- \`/api/auth/register/\`: User registration
- \`/api/auth/login/\`: User login

## Usage

To upload a file, use a POST request to \`/files/\`.

To download a file, navigate to \`/files/<id>\`.
