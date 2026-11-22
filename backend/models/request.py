from pydantic import BaseModel, field_validator

class StartupRequest(BaseModel):

    idea: str

    @field_validator("idea")
    @classmethod
    def validate_idea(cls, v):
        v=v.strip()
        if len(v) == 0:
            raise ValueError("Idea is required")
        if len(v) > 2000:
            raise ValueError("Idea must be 2000 characters or less.")
        return v