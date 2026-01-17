Backend Developer Assignment - Django & PostgreSQL
This project is a task management API built using Django and Django REST Framework (DRF) as part of the evaluation for the Backend Developer position at Proteger AI Pvt Ltd.
1. Setup Instructions 

Follow these steps to initialize the project environment:

Clone the repository: Navigate to the project folder in your terminal.

Create a Virtual Environment: python -m venv venv

Activate the Environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install Dependencies:
pip install django djangorestframework psycopg2-binary python-dotenv

2. PostgreSQL Configuration 

The project uses environment variables for secure database configuration.

Create a .env file in the root directory of the project.

Add the following variables (update with your local PostgreSQL credentials):

DB_NAME=proteger_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

3. Migration Commands 

Prepare the database schema by running these commands:

Generate Migrations:

python manage.py makemigrations

Apply Migrations:

python manage.py migrate

Create Admin User:

python manage.py createsuperuser

4. Sample API Requests 

Below are examples of how to interact with the API endpoints.

User Endpoints

Create User (POST /users/): 

JSON

{
    "username": "ganesh_dev",
    "email": "delliganeshn97@gmail.com"
}

List Users (GET /users/):  Returns a list of all registered users.

Task Endpoints

Create Task (POST /tasks/): 

JSON

{
    "title": "Build Django API",
    "description": "Complete the Proteger AI assignment",
    "status": "In Progress",
    "user": 1
}

List Tasks (GET /tasks/): 


Filter Tasks by Status (GET /tasks/?status=Completed): 


Update Task (PUT /tasks/{id}/): 


Delete Task (DELETE /tasks/{id}/): 


Submission Deadline: 17-Jan-2026 before 04:00 PM.