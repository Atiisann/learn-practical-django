FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y postgresql netcat

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /code/
