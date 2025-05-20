# food_pantry_management

Non-profit Food Pantry Management System

## Database Migrations
This project uses Flask-Migrate with a PostgreSQL database. After installing dependencies, set the `DATABASE_URL` environment variable or ensure Postgres is running locally and initialize the migration repository with:

```bash
flask db init
flask db migrate -m "create user table"
flask db upgrade
```

This repo contains a simple Flask application demonstrating role-based
access control. The decorators in `pantry/decorators.py` provide helper
wrappers to ensure that a user has the correct role before accessing a
view. The included `admin_required`, `staff_required`, and
`volunteer_required` decorators can be applied to any route.

Run the application with `python app.py` and visit `/login/<role>` to
simulate logging in as a user. The admin dashboard located at
`/admin/dashboard` is protected with `@admin_required`.

