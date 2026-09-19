import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.product_service import (create_product_service, get_product_service, get_products_service, update_product_service)


router = APIRouter(prefix="/product", tags=['Products']) # will add /products after every route and tags are mainly for swagger doc

#schema for craeting product
class ProductCreate(BaseModel):
    name: str
    description : str
    sku : str
    price : float
    category: str
    status: str

class ProductUpdate(BaseModel):
    name: Optional[str]= None
    description: Optional[str]=None
    sku: Optional[str]=None
    price: Optional[float]=None
    category:Optional[str]=None
    status:Optional[str]=None

class ProductResponse(ProductCreate):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID

#create a product
@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db:Session=Depends(get_db)):
    
    try:
        return create_product_service(db, product)
    except IntegrityError as e:
        db.rollback()
        print(e.orig)
        raise HTTPException(status_code=409, detail=" a product with this sku already exist")
    

    




#get all the products
@router.get("/getProducts", response_model=list[ProductResponse])
def get_products(db:Session=Depends(get_db)):
    return get_products_service(db)

#return the product
@router.get("/{id}", response_model=ProductResponse)
def get_product(id: uuid.UUID, db:Session=Depends(get_db)):
    product = get_product_service(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product

@router.patch("/{id}", response_model=ProductResponse)
def update_product(id: uuid.UUID, product_update:ProductUpdate, db: Session = Depends(get_db)):
    product = update_product_service(db, id, product_update)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product

