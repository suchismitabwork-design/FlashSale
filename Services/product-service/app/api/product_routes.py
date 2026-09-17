import uuid

from fastapi import APIRouter
#to create a router which can be joined in main.py
from pydantic import BaseModel
#pydantic for schema
import datetime # to generate datetime
from uuid import uuid4  # to generate random id 

router = APIRouter(prefix="/product", tags=['Products']) # will add /products after every route and tags are mainly for swagger doc

product_bucket = []

#schema for craeting product
class ProductCreate(BaseModel):
    name : str
    description : str
    sku : str
    price : float
    category : str
    status : str


#create a product
@router.post("/")
def create_product(product: ProductCreate):
    
    now = datetime.datetime.now(datetime.timezone.utc)
    new_product = {
        "id" : str(uuid.uuid4()),
        **product.model_dump(),
        "created_at" : now,
        "updated_at" : now
    }
    product_bucket.append(new_product) # storing our created products into product_bucket
    return{
        "message": "The post has been successfully created",
        "product" : new_product
           }



#get all the products
@router.get("/getProducts")
def get_products():
    return {"message" : "Get all products",
            "products" : product_bucket
            }

#return the product
@router.get("/{id}")
def get_product(id: str):
    for product in product_bucket : 
        if product["id"] == id:
            return product
    return {"message" : "product not found !"}

@router.patch("/{update}")
def update_prod(id : str, product_update: ProductCreate):

    for prod in product_bucket:
        if prod["id"] == id:
            updates = product_update.model_dump(exclude_unset=True)
            prod.update(updates)
            prod["updated_at"] = datetime.datetime.now(datetime.timezone.utc)

            return {
                "message" : "Product has been successfully updated",
                "product" : prod
            }
    return {"message" : "Product not Found !"}


@router.delete("/{id}")
def delete_post(id: str):
    for prod in product_bucket:
        if prod["id"] == id:
            product_bucket.remove(prod)
            return {"message" : "product successfully deleted",
                    "product" : prod
                    }
    return {"message" : "Product doesnot exist"}
        
            
        
