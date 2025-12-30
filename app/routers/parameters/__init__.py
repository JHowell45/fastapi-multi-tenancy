from pydantic import BaseModel, Field


class GeneralParameters(BaseModel):
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=100, gt=0, le=200)
