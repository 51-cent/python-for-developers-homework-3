from fastapi import APIRouter, HTTPException

from app.shemas.calculate import CalculateRequest, CalculateResponse
from app.services.calculate import calc_all

router = APIRouter()


@router.post("/", response_model=CalculateResponse)
async def calculate(data: CalculateRequest):
    if len(data.numbers) != len(data.delays):
        raise HTTPException(status_code=400, detail="Длина полей numbers и delays должна быть одинаковой")

    return await calc_all(data.numbers, data.delays)
