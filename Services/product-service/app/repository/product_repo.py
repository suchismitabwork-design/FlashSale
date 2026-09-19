from sqlalchemy.orm import Session
from app.models.models import Product


def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db:Session):
    return db.query(Product).all()
    
def get_product_by_id(db:Session, product_id):
    return db.query(Product).filter_by(id=product_id).first()
    

def update_product(db: Session, product: Product, update:dict):
    for key, value in update.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


