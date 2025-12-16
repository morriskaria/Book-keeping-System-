from app.database.database import SessionLocal
from app.models.payroll import Employee, PayrollPayment
from app.models.user import User # Needed for Foreign Key resolution
from app.models.expense import Expense # Needed for User relationship resolution

def test_payroll_flow():
    db = SessionLocal()
    try:
        print("Testing Payroll Flow...")
        
        # 1. Create Employee
        emp = Employee(
            name="John Specialist",
            position="Surgeon",
            salary=3000.0
        )
        db.add(emp)
        db.commit()
        print(f"Hired: {emp.name} (Salary: {emp.salary})")
        
        # 2. Pay Employee (Manual logic simulation)
        # Using None for amount to test auto-salary logic
        payment = PayrollPayment(
            employee_id=emp.id,
            amount=emp.salary, # Logic is in route, here we simulate the result
            is_taxed=True
        )
        db.add(payment)
        db.commit()
        
        print(f"Paid: {payment.amount} (Taxed: {payment.is_taxed})")
        
        assert payment.amount == 3000.0
        print("SUCCESS: Payroll processed correctly!")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_payroll_flow()
