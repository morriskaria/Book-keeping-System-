from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import database
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.routes.auth import oauth2_scheme # In future, we use get_current_user to link recorder

router = APIRouter()

@router.post("/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(database.get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(db: Session = Depends(database.get_db)):
    return db.query(Expense).all()
