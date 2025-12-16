from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.expense import ExpenseCategory

class ExpenseBase(BaseModel):
    title: str
    amount: float = Field(..., gt=0, description="Expense amount must be positive")
    category: ExpenseCategory = ExpenseCategory.OTHER
    description: Optional[str] = None
    expense_date: Optional[datetime] = None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    expense_date: datetime
    class Config:
        from_attributes = True
