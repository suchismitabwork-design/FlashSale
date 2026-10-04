
# this section contains all routes that are involves in order service : ideally we should have 2, 3 route files conncted in a router file.

# POST/orders , GET/orders, GET/order/{id} , POST/order/{id}/cancel
''' steps for creating route page 
1. import APIrouter(for defining routes), pydantic basemodel (schema)
2. define a orderCreate schema (pydantic schema)

'''

from fastapi import APIRouter
from app.schema.schema import orderCreate, orderResponse, orderItemResponse, orderItemCreate

router = APIRouter(prefix='/order', tags=['orders'])

@router.post("/")
def create_order(order: orderCreate):
    return order

