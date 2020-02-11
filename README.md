# Bones
A simple application that demonstrates [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) and serves as a modern Python application skeleton.

### Setup

1. Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. `$ docker-compose up`
3. Check app health: `GET http://127.0.0.1:8080/v1/health-check`
4. Create env file (and populate as necessary): `$ touch src/.env`

### Development

* Update dependencies: `$ docker-compose build app`

### Testing

### Todo

1. ~~Add Nginx~~
2. ~~Add view presenter~~
3. Tests
4. ~~Validation~~
5. ~~Server hot-reloading~~
6. Request level validation
7. Dev and prod settings
8. ~~Integrate .env~~
