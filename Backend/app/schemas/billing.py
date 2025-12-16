from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.models.billing import InvoiceStatus, PaymentMethod

# --- Patient Schemas ---
class PatientBase(BaseModel):
    name: str
    phone: Optional[str] = None
    age: int

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- Service Schemas ---
class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be positive")

class ServiceCreate(ServiceBase):
    pass

class ServiceResponse(ServiceBase):
    id: int
    class Config:
        from_attributes = True

# --- Payment Schemas ---
class PaymentCreate(BaseModel):
    invoice_id: int
    amount: float = Field(..., gt=0, description="Payment amount must be positive")
    payment_method: PaymentMethod = PaymentMethod.CASH
    transaction_id: Optional[str] = None

class PaymentResponse(BaseModel):
    id: int
    amount: float
    payment_method: PaymentMethod
    payment_date: datetime
    class Config:
        from_attributes = True

# --- Invoice Schemas ---
class InvoiceItemCreate(BaseModel):
    service_id: int
    quantity: int = Field(1, gt=0, description="Quantity must be at least 1")

class InvoiceCreate(BaseModel):
    patient_id: int
    items: List[InvoiceItemCreate]

class InvoiceItemResponse(BaseModel):
    id: int
    service_name: str
    unit_price: float
    quantity: int
    class Config:
        from_attributes = True

class InvoiceResponse(BaseModel):
    id: int
    patient_id: int
    total_amount: float
    paid_amount: float
    status: InvoiceStatus
    created_at: datetime
    items: List[InvoiceItemResponse] = []
    payments: List[PaymentResponse] = [] # Show payments on invoice
    
    class Config:
        from_attributes = True
