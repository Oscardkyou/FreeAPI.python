from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum

class ShipmentType(enum.Enum):
    AUTO = "auto"
    RAIL = "rail"
    SEA = "sea"

class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True, index=True)
    from_city = Column(String, nullable=False)
    to_city = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    shipment_type = Column(Enum(ShipmentType), nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
