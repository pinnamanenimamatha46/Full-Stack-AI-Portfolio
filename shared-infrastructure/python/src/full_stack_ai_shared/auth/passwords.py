"""Password hashing and verification utilities."""

from pwdlib import PasswordHash

_password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Return a secure hash for a plaintext password."""

    if not password:
        raise ValueError("Password cannot be empty.")

    return _password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """Return whether a plaintext password matches a stored hash."""

    if not plain_password or not hashed_password:
        return False

    return _password_hash.verify(
        plain_password,
        hashed_password,
    )
