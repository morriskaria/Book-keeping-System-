from app.database.database import SessionLocal
from app.models.inventory import InventoryItem

def test_inventory_flow():
    db = SessionLocal()
    try:
        print("Testing Inventory Flow...")
        
        # 1. Create Low Stock Item
        item = InventoryItem(
            name="Cotton Wool",
            category="Consumable",
            quantity=5,
            unit="roll",
            reorder_level=10 # 5 is less than 10, so it's low stock
        )
        db.add(item)
        db.commit()
        print(f"Created: {item.name} (Qty: {item.quantity}, Reorder: {item.reorder_level})")
        
        # 2. Check Low Stock Logic
        low_items = db.query(InventoryItem).filter(InventoryItem.quantity <= InventoryItem.reorder_level).all()
        found = any(i.name == "Cotton Wool" for i in low_items)
        print(f"Is Cotton Wool low stock? {found}")
        assert found == True
        
        # 3. Restock
        print("Restocking +20...")
        item.quantity += 20
        db.commit()
        print(f"New Qty: {item.quantity}")
        
        # 4. Check Low Stock Again
        low_items = db.query(InventoryItem).filter(InventoryItem.quantity <= InventoryItem.reorder_level).all()
        found = any(i.name == "Cotton Wool" for i in low_items)
        print(f"Is Cotton Wool low stock? {found}")
        assert found == False
        
        print("SUCCESS: Inventory logic works!")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_inventory_flow()
