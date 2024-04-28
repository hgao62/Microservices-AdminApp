FROM python:3.9

# Install system dependencies
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

ENV PYTHONNUBBUFFERD 1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000