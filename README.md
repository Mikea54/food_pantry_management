# food_pantry_management
Non-profit Food Pantry Management System

## Database Migrations
This project uses Flask-Migrate with a PostgreSQL database. After installing dependencies, set the `DATABASE_URL` environment variable or ensure Postgres is running locally and initialize the migration repository with:

```bash
flask db init
flask db migrate -m "create user table"
flask db upgrade
```

