# Food Pantry Management

This project contains a small Flask application demonstrating user authentication and role based access control for a food pantry. It is intended as a learning example and includes tests for the basic models and decorators.

## Features

- Flask application structured as a package in `app/` with blueprints
- Login and logout views with Flask-Login
- `User` model using SQLAlchemy with roles (`admin`, `user`, `staff`, `volunteer`)
- Admin area for creating users
- User dashboard page
- Role protected decorators in `pantry/decorators.py`

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. By default the application uses SQLite and stores data in `pantry.db`. To use another database set the `DATABASE_URL` environment variable.

3. Initialize the database (only required the first time):

   ```bash
   flask db init
   flask db migrate -m "create user table"
   flask db upgrade
   ```

## Running the App

Run the development server with:

```bash
python run.py
```

The main routes are:

- `/` – simple greeting
- `/login` – log in with email and password
- `/logout` – log out the current user
- `/dashboard` – user dashboard (requires login)
- `/admin` – admin dashboard (requires admin role)
- `/admin/users/new` – form to create new users
- `/intake` – household intake form

## Tests

The repository includes basic tests for user creation, password hashing and role
checking. Run them with:

```bash
pytest
```




