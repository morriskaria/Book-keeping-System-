from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String) # e.g. Nurse, Cleaner, Security
    salary = Column(Float) # Monthly base salary
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    # Optional link to a system user (if they have a login)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    payments = relationship("PayrollPayment", back_populates="employee")

class PayrollPayment(Base):
    __tablename__ = "payroll_payments"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    amount = Column(Float)
    payment_date = Column(DateTime, default=datetime.utcnow)
    is_taxed = Column(Boolean, default=False)
    
    employee = relationship("Employee", back_populates="payments")
