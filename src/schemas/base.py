from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
