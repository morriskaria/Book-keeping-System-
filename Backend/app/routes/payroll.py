from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import database
from app.models.payroll import Employee, PayrollPayment
from app.schemas.payroll import EmployeeCreate, EmployeeResponse, PayrollPaymentCreate, PayrollPaymentResponse

router = APIRouter()

# --- EMPLOYEES ---
@router.post("/staff", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(database.get_db)):
    db_emp = Employee(**employee.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

@router.get("/staff", response_model=List[EmployeeResponse])
def get_staff(db: Session = Depends(database.get_db)):
    return db.query(Employee).all()

# --- PAYROLL PAYMENTS ---
@router.post("/payroll", response_model=PayrollPaymentResponse)
def pay_staff(payment_data: PayrollPaymentCreate, db: Session = Depends(database.get_db)):
    # 1. Check Employee
    employee = db.query(Employee).filter(Employee.id == payment_data.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # 2. Determine Amount (Use base salary if not provided)
    amount_to_pay = payment_data.amount if payment_data.amount else employee.salary

    # 3. Create Record
    payment = PayrollPayment(
        employee_id=employee.id,
        amount=amount_to_pay,
        is_taxed=payment_data.is_taxed
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
