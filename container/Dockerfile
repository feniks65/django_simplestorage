FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# TODO uncomment when ready for deployment
#CMD ["gunicorn", "storage.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT /bin/bash

