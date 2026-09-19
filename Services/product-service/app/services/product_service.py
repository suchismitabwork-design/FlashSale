from sqlalchemy.orm import Session
from app.models.models import Product
from app.repository.product_repo import create_product, get_all_products, get_product_by_id, update_product

def create_product_service(db:Session, product_data):

    product = Product(**product_data.model_dump())
    return create_product(db,product)

def get_products_service(db:Session):
    return get_all_products(db)

def get_product_service(db:Session, product_id):
    return get_product_by_id(db, product_id)

def update_product_service(db:Session, product_id, product_update):
    product = get_product_by_id(db, product_id)
    if not product:
        return None
    update = product_update.model_dump(exclude_unset=True)
    return update_product(db, product, update)
