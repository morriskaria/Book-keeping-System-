from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    category = Column(String) # e.g. "Medicine", "Equipment"
    quantity = Column(Integer, default=0)
    unit = Column(String) # e.g. "Box", "Pcs"
    reorder_level = Column(Integer, default=10) # Alert if below this
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
