from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@dataclass
class User(UserMixin):
    id: int
    email: str
    password_hash: str
    role: str

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


# In-memory user store for example purposes
users = {
    1: User(id=1, email="admin@example.com", password_hash=generate_password_hash("admin"), role="admin"),
    2: User(id=2, email="user@example.com", password_hash=generate_password_hash("user"), role="user"),
}


def get_user_by_email(email: str) -> User | None:
    for user in users.values():
        if user.email == email:
            return user
    return None
