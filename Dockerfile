FROM python:3.8-alpine
# force stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1
# no .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
