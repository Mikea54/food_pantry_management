# food_pantry_management

Non-profit Food Pantry Management System

This repo contains a simple Flask application demonstrating role-based
access control. The decorators in `pantry/decorators.py` provide helper
wrappers to ensure that a user has the correct role before accessing a
view. The included `admin_required`, `staff_required`, and
`volunteer_required` decorators can be applied to any route.

Run the application with `python app.py` and visit `/login/<role>` to
simulate logging in as a user. The admin dashboard located at
`/admin/dashboard` is protected with `@admin_required`.
