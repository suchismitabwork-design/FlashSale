import uuid

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey, Numeric
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base

class orderItem(Base):

    __tablename__ = "order_items"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, nullable=True, default=uuid.uuid4)
    order_id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey("orders.id"),nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[Numeric] = mapped_column(Numeric(10,2), nullable=False)
    total_price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    order = relationship("order", back_populates="items")

