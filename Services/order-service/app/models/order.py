
import uuid
from datetime import datetime
from sqlalchemy import DateTime, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.models.base import Base

class order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False,)
    total_amount: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    items = relationship("orderItem", back_populates="order")
    