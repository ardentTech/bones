# Bones
A simple application that demonstrates [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) and serves as a modern Python application skeleton.

### Setup

1. Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. `$ docker-compose up`
3. Check app health http://127.0.0.1:8000/v1/health-check

### Development

* Update dependencies: `$ docker-compose build app`

### Testing

### Warning

1. Gunicorn is sitting on 0.0.0.0, but should be behind a reverse proxy (Nginx) in production.

### Todo

1. Add Nginx
2. ~~Add view presenter~~
3. Tests
4. ~~Validation~~
5. Docker hot-reloading
6. Request level validation
