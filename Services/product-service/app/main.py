from fastapi import FastAPI
from app.api.product_routes import router as product_router

app = FastAPI()

app.include_router(product_router)

