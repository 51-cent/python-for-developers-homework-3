from pydantic import BaseModel


class CalculateRequest(BaseModel):
    numbers: list[int]
    delays: list[float]


class CalculateResult(BaseModel):
    number: int
    square: int
    delay: float
    time: float


class CalculateResponse(BaseModel):
    results: list[CalculateResult]
    total_time: float
    parallel_faster_than_sequential: bool
