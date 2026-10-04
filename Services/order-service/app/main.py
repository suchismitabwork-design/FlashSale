
# main connector for our order service

from fastapi import FastAPI
from app.api.order_routes import router

app = FastAPI()
app.include_router(router)