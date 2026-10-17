from fastapi import FastAPI

from app.routes.calculate import router as calculate_router

app = FastAPI(title="Домашнее задание 3. Асинхронность в Python")

app.include_router(calculate_router, prefix="/calculate", tags=["calculate"])
