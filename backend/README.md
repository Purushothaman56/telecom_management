```markdown
# Telecom Customer Management System (TCMS)

This project is a web-based application to manage and track telecom mobility customers. It includes functionalities for registering new customers, assigning plans, renewing plans, upgrading/downgrading plans, and displaying customer data in a tabular format.

## Requirements
- Python 3.7 or higher
- A virtual environment tool (such as `venv` or `virtualenv`)
- Basic knowledge of Flask, SQLAlchemy, and migrations

## Project Structure
Here's an overview of the project structure:
```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── ...
├── tests/
│   ├── __init__.py
│   ├── test_customer.py
│   ├── ...
├── config_test.py
├── wsgi.py
├── requirements.txt
```

## Setup
Follow these steps to set up the project:

1. **Create and Activate a Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   Install Flask, SQLAlchemy, Flask-Migrate, and other dependencies.
   ```
   pip install -r requirements.txt
   ```

3. **Create the SQLite Database**
   ```
   touch telecom.db
   ```

4. **Run the Flask Application**
   Use Gunicorn to run the Flask application.
   ```
   # Run the application using Gunicorn
   gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app
   ```

## Database Migrations
To set up migrations, ensure Flask-Migrate is installed and initialized in the project. Follow these steps to migrate the database:

1. **Initialize Migrations**
   This step creates the necessary migration files and setup.
   ```
   flask db init
   ```

2. **Generate a Migration Script**
   This step generates the migration script based on the current database schema.
   ```
   flask db migrate -m "Initial migration"
   ```

3. **Apply the Migration**
   This step applies the migration to the database, updating the schema.
   ```
   flask db upgrade
   ```

## Running Tests
Ensure that the `tests/` folder contains the unit tests. Here's how to run the tests and ensure proper import paths:

1. **Set the Python Path**
   Ensure the project root is in the `PYTHONPATH`.
   ```
   # Set PYTHONPATH to the project root
   export PYTHONPATH=$(pwd)
   ```

2. **Run the Tests**
   Use `pytest` to run the tests.
   ```
   pytest tests/
   ```

## Checking Test Coverage
To check test coverage, use `pytest-cov`. This tool provides a report indicating the proportion of code executed during tests:

1. **Install `pytest-cov`**
   ```
   pip install pytest-cov
   ```

2. **Run Tests with Coverage Reporting**
   ```
   pytest --cov=app tests/
   ```

This command generates a test coverage report for the `app` module based on the tests in the `tests/` folder.

## Running the Project with Docker Compose
To run your project using Docker Compose, follow these steps:

1. **Build the Docker images and start the containers**
  ```
  docker-compose up --build
  ```
The --build option ensures the Docker image is rebuilt with any changes in the Dockerfile or source code.
Access the Application
Once Docker Compose has started the container, you can access the application at http://localhost:8000 or the appropriate bound address.

2. **Stopping the Containers**
  ```
  docker-compose down
  ```

## API Endpoints
- **Customer Endpoints**
  - `POST /customers`: Register a new customer.
  - `GET /customers`: Retrieve all customers.
  - `GET /customers/{customer_id}`: Retrieve a specific customer's details. **Skipped**
  - `PUT /customers/{customer_id}`: Update a customer's details.
  - `DELETE /customers/{customer_id}`: Delete a customer.
- **Plan Endpoints**
  - `GET /plans`: Retrieve all available plans.
  - `POST /plans`: Add a new plan.
- **Renewal Endpoints**
  - `POST /renewals`: Record a plan renewal.
  - `GET /renewals`: Retrieve all renewals. **Skipped**
