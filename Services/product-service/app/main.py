from fastapi import FastAPI
from app.api.product_routes import router as product_router
from app.db.database import Base, engine
from app.models import models

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(product_router)

