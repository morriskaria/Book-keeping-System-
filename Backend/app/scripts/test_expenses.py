from app.database.database import SessionLocal
from app.models.expense import Expense, ExpenseCategory
from app.models.user import User # Import needed so SQLAlchemy sees the User model for the relationship

def test_expense_flow():
    db = SessionLocal()
    try:
        print("Testing Expense Flow...")
        
        # 1. Create Expenses
        ex1 = Expense(
            title="Surgical Gloves",
            amount=50.0,
            category=ExpenseCategory.MEDICAL_SUPPLIES,
            description="Box of 100"
        )
        db.add(ex1)
        
        ex2 = Expense(
            title="Electricity Bill",
            amount=150.0,
            category=ExpenseCategory.UTILITIES,
            description="January 2025"
        )
        db.add(ex2)
        
        db.commit()
        print("created expenses")
        
        # 2. List Expenses
        expenses = db.query(Expense).all()
        print(f"Total Expenses found: {len(expenses)}")
        for ex in expenses:
            print(f"- {ex.title} ({ex.category.value}): KSh {ex.amount}")
            
        assert len(expenses) >= 2
        print("SUCCESS: Expenses tracked correctly!")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_expense_flow()
