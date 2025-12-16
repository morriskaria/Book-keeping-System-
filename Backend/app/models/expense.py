from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database.database import Base

class ExpenseCategory(str, enum.Enum):
    MEDICAL_SUPPLIES = "medical_supplies"
    UTILITIES = "utilities"
    SALARIES = "salaries"
    MAINTENANCE = "maintenance"
    RENT = "rent"
    OTHER = "other"

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    amount = Column(Float)
    category = Column(Enum(ExpenseCategory), default=ExpenseCategory.OTHER)
    description = Column(String, nullable=True)
    expense_date = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to User
    # We use "User" as a string to avoid circular imports. 
    # SQLAlchemy resolves this string to the actual class later.
    recorder_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    recorder = relationship("User", back_populates="expenses")

