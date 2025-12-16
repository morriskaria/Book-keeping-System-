from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import Optional

from app.database import database
from app.models.billing import Payment
from app.models.expense import Expense
from app.models.payroll import PayrollPayment
from app.schemas.report import FinancialSummary

router = APIRouter()

@router.get("/summary", response_model=FinancialSummary)
def get_financial_summary(
    start_date: Optional[datetime] = None, 
    end_date: Optional[datetime] = None, 
    db: Session = Depends(database.get_db)
):
    # Default to "All Time" if not provided, or logic can be "This Month"
    # For flexibility, if None, we query everything.
    
    # 1. Revenue (Sum of Payments)
    query_rev = db.query(func.sum(Payment.amount))
    if start_date:
        query_rev = query_rev.filter(Payment.payment_date >= start_date)
    if end_date:
        query_rev = query_rev.filter(Payment.payment_date <= end_date)
    total_revenue = query_rev.scalar() or 0.0

    # 2. Operational Expenses
    query_exp = db.query(func.sum(Expense.amount))
    if start_date:
        query_exp = query_exp.filter(Expense.expense_date >= start_date)
    if end_date:
        query_exp = query_exp.filter(Expense.expense_date <= end_date)
    total_expenses = query_exp.scalar() or 0.0

    # 3. Payroll Expenses
    query_pay = db.query(func.sum(PayrollPayment.amount))
    if start_date:
        query_pay = query_pay.filter(PayrollPayment.payment_date >= start_date)
    if end_date:
        query_pay = query_pay.filter(PayrollPayment.payment_date <= end_date)
    total_payroll = query_pay.scalar() or 0.0

    # 4. Profit
    net_profit = total_revenue - (total_expenses + total_payroll)

    return FinancialSummary(
        start_date=start_date,
        end_date=end_date,
        total_revenue=total_revenue,
        total_expenses=total_expenses,
        total_payroll=total_payroll,
        net_profit=net_profit
    )
