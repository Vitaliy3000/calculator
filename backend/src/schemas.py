from pydantic import BaseModel, Field


class SumRequestModel(BaseModel):
    number1: int = Field(gt=0)
    number2: int = Field(ge=0)


class SumResponseModel(BaseModel):
    result: int = Field(gt=0)
