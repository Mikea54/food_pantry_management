"""Re-export models from the project root for use within the application.
This avoids keeping duplicate model definitions in multiple modules.
"""

from models import (
    db,
    User,
    Household,
    HouseholdMember,
    get_user_by_email,
)

__all__ = [
    "db",
    "User",
    "Household",
    "HouseholdMember",
    "get_user_by_email",
]
