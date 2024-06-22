# FastAPI + Prisma + PostgreSQL + Docker Template

## Overview

This repository provides a template for setting up a FastAPI application integrated with Prisma as the ORM and PostgreSQL as the database, all containerized using Docker. This template is designed to help you quickly get started with building scalable and maintainable backend applications.

## Features

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Prisma**: A modern database toolkit and ORM that replaces traditional ORMs.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Docker**: Containerization for easy deployment and development.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.11 or higher installed on your machine.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/omauriciomaciel/fastapi-prisma-postgresql-docker-template.git
cd fastapi-prisma-postgresql-docker-template
```

### 2. Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```env
DATABASE_URL="postgres://postgres:password@db:5432/dbname?schema=public"
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=dbname
```

### 3. Docker Setup

Build and run the Docker containers:

```bash
docker-compose up --build
```

This will start the FastAPI application, Prisma, and PostgreSQL containers.

### 4. Running Migrations

Make sure to generate the Prisma client and apply migrations:

```bash
docker-compose exec backend prisma generate
docker-compose exec backend prisma migrate deploy
```

### 5. Access the Application

Your FastAPI application will be available at `http://localhost:8000`.

### 6. API Documentation

FastAPI provides interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
fastapi-prisma-postgresql-docker-template
│
├── services
│   ├── backend
│   │   ├── api
│   │   │   ├── routers
│   │   │   │   └── user.py
│   │   │   ├── schemas
│   │   │   │   └── user.py
│   │   │   ├── services
│   │   │   │   └── user.py
│   │   │   ├── connection.py
│   │   │   ├── main.py
│   │   ├── prisma
│   │   │   └── schema.prisma
│   │   ├── Dockerfile
│   │   ├── requirements.txt│
├── .env
├── docker-compose.yml
```

## Key Files

- **main.py**: The entry point of the FastAPI application.
- **connection.py**: Manages the Prisma database connection lifecycle.
- **routers/user.py**: Contains the API endpoints related to user operations.
- **schemas/user.py**: Defines the data models for user operations.
- **services/user.py**: Contains the business logic for user operations.
- **prisma/schema.prisma**: Prisma schema definition.

## Usage

### Creating a User

To create a new user, send a POST request to `/user/` with the following payload:

```json
{
  "username": "exampleuser"
}
```

### Retrieving Users

To retrieve a list of users, send a GET request to `/user/`.

### Retrieving a User by ID

To retrieve a user by their ID, send a GET request to `/user/{user_id}`.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This template aims to provide a solid foundation for your FastAPI projects with Prisma, PostgreSQL, and Docker. Happy coding!