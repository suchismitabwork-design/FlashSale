from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid

# routes should never talk directly to services

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    sku = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String)
    status = Column(String)





    

