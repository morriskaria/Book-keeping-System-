from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import database
from app.models.inventory import InventoryItem
from app.schemas.inventory import InventoryCreate, InventoryResponse, InventoryRestock

router = APIRouter()

@router.post("/", response_model=InventoryResponse)
def create_item(item: InventoryCreate, db: Session = Depends(database.get_db)):
    # Check if exists
    exists = db.query(InventoryItem).filter(InventoryItem.name == item.name).first()
    if exists:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    new_item = InventoryItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=List[InventoryResponse])
def get_inventory(db: Session = Depends(database.get_db)):
    return db.query(InventoryItem).all()

@router.get("/low-stock", response_model=List[InventoryResponse])
def get_low_stock(db: Session = Depends(database.get_db)):
    """Return items that are below or equal to the reorder level."""
    return db.query(InventoryItem).filter(InventoryItem.quantity <= InventoryItem.reorder_level).all()

@router.post("/{item_id}/restock", response_model=InventoryResponse)
def restock_item(item_id: int, restock: InventoryRestock, db: Session = Depends(database.get_db)):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item.quantity += restock.quantity_to_add
    db.commit()
    db.refresh(item)
    return item
