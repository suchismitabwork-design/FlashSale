 # schemas will have pydantic schemas that our APIs will accept as req and res
from pydantic import BaseModel, Field, ConfigDict
import uuid

class orderItemCreate(BaseModel):
    product_id : uuid.UUID
    quantity : int=Field(gt=0)
class orderCreate(BaseModel):
    items : list[orderItemCreate]
class orderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) # if your DB is returning an SQl alchemy object, we can access its data like product.id, bt pydantic accepts dict
    id : uuid.UUID
    status: str
    total_amount : float
    items: list[orderItemCreate]
class orderItemResponse(BaseModel): # these extra values comes from product service 
    model_config = ConfigDict(from_attributes=True)
    product_id : uuid.UUID
    quantity:int
    unit_price: int
    total_price: int