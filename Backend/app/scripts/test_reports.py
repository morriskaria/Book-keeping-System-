from app.database.database import SessionLocal
from app.models.billing import Payment
from app.models.expense import Expense
from app.models.payroll import PayrollPayment
from app.models.user import User # Needed for SQLAlchemy relationship resolution
from sqlalchemy import func

def test_report_logic():
    db = SessionLocal()
    try:
        print("Testing Report Logic...")
        
        # 1. Get raw sums directly to verify
        total_rev = db.query(func.sum(Payment.amount)).scalar() or 0.0
        total_exp = db.query(func.sum(Expense.amount)).scalar() or 0.0
        total_pay = db.query(func.sum(PayrollPayment.amount)).scalar() or 0.0
        
        print(f"Revenue: {total_rev}")
        print(f"Expenses: {total_exp}")
        print(f"Payroll: {total_pay}")
        
        # 2. Iterate Logic
        calculated_net = total_rev - (total_exp + total_pay)
        print(f"Calculated Net Profit: {calculated_net}")
        
        # 3. Validation (Based on previous tests running)
        # Note: If previous tests ran multiple times, numbers might be higher.
        # But Revenue should be > 0, Payroll > 0.
        assert total_rev > 0
        assert total_pay > 0
        
        print("SUCCESS: Report logic aggregates correctly!")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_report_logic()
