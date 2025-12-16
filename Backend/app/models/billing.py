from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database.database import Base

class InvoiceStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    invoices = relationship("Invoice", back_populates="patient")

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    price = Column(Float) # Default price

class PaymentMethod(str, enum.Enum):
    CASH = "cash"
    CARD = "card"
    INSURANCE = "insurance"
    MPESA = "mpesa"

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    total_amount = Column(Float, default=0.0)
    paid_amount = Column(Float, default=0.0)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")
    payments = relationship("Payment", back_populates="invoice")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    service_name = Column(String) # Snapshot of name at time of billing
    unit_price = Column(Float)    # Snapshot of price at time of billing
    quantity = Column(Integer, default=1)
    
    invoice = relationship("Invoice", back_populates="items")
    service = relationship("Service")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    amount = Column(Float)
    payment_method = Column(Enum(PaymentMethod), default=PaymentMethod.CASH)
    transaction_id = Column(String, nullable=True) # e.g. M-Pesa Code
    payment_date = Column(DateTime, default=datetime.utcnow)

    invoice = relationship("Invoice", back_populates="payments")
