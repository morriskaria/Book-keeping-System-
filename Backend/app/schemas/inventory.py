from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class InventoryBase(BaseModel):
    name: str
    category: str
    quantity: int = Field(0, ge=0, description="Quantity cannot be negative")
    unit: str
    reorder_level: int = 10

class InventoryCreate(InventoryBase):
    pass

class InventoryRestock(BaseModel):
    quantity_to_add: int = Field(..., gt=0, description="Must add at least 1 item")

class InventoryResponse(InventoryBase):
    id: int
    last_updated: datetime
    class Config:
        from_attributes = True
