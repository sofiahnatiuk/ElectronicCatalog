# ElectronicCatalog
A Django-based web application that allows users to browse, search, and filter a catalog of electronic components. Supports nested categories, component details with dynamic specifications, and user accounts. My bachelor's diploma project

## Features

- Component listings with filters by category, manufacturer, etc.
- Component detail pages with dynamic specs
- Admin panel to manage categories and components
- REST API using Django REST Framework
- Swagger documentation for the API
- Basic user accounts (registration, login, etc.)

  ## Tech Stack

- Python 3.12+
- Django 4.2
- Django REST Framework
- PostgreSQL
- Bootstrap 5 (for frontend)
- Swagger (drf-spectacular)
- Docker

## Installation

### Prerequisites

- Docker

### 1. Clone the repo

```bash
git clone https://github.com/sofiahnatiuk/ElectronicCatalog.git
cd ElectronicCatalog
```

### 2. Build and run Docker containers
```bash
docker-compose up --build
```

### 3. View API documentation
http://localhost:8000/api/docs/
