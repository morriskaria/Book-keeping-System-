from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FinancialSummary(BaseModel):
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    total_revenue: float
    total_expenses: float
    total_payroll: float
    net_profit: float
