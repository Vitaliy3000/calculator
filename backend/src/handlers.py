from fastapi import FastAPI

import schemas


app = FastAPI(title="Calculator")


@app.post("/calc", response_model=schemas.SumResponseModel)
def calc(numbers: schemas.SumRequestModel):
    result = numbers.number1 + numbers.number2
    return schemas.SumResponseModel(result=result)
