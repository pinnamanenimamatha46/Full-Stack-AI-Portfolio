"""Authentication and token settings."""

from pydantic import BaseModel, Field


class TokenSettings(BaseModel):
    """JWT configuration."""

    secret_key: str = Field(min_length=32)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(default=30, gt=0)
    issuer: str = "full-stack-ai-portfolio"
    audience: str = "full-stack-ai-applications"
