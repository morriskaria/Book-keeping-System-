from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# --- Employee Schemas ---
class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: float = Field(..., gt=0, description="Salary must be positive")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    joined_at: datetime
    class Config:
        from_attributes = True

# --- Payment Schemas ---
class PayrollPaymentCreate(BaseModel):
    employee_id: int
    amount: Optional[float] = None # If None, use base salary
    is_taxed: bool = False

class PayrollPaymentResponse(BaseModel):
    id: int
    employee_id: int
    amount: float
    payment_date: datetime
    class Config:
        from_attributes = True
