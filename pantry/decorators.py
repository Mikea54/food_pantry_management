from functools import wraps
from flask import abort
from flask_login import current_user


def role_required(role):
    """Return decorator that checks for a user role."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not getattr(current_user, "is_authenticated", False) or getattr(current_user, "role", None) != role:
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def admin_required(func):
    return role_required("admin")(func)


def staff_required(func):
    return role_required("staff")(func)


def volunteer_required(func):
    return role_required("volunteer")(func)
