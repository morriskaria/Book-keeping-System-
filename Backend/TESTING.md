# Developer Testing Guide

## Setup
1. Ensure your virtual environment is active:
   ```powershell
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running Tests
We have a suite of scripts in `app/scripts/` to verify each module.

### Run All Tests
To check the entire system health at once:
```powershell
$env:PYTHONPATH="."
python app/scripts/run_all_tests.py
```

### Individual Module Tests
- **Billing**: `python app/scripts/test_billing.py`
- **Payments**: `python app/scripts/test_payments.py`
- **Expenses**: `python app/scripts/test_expenses.py`
- **Payroll**: `python app/scripts/test_payroll.py`
- **Inventory**: `python app/scripts/test_inventory.py`
- **Reports**: `python app/scripts/test_reports.py`
- **Validation**: `python app/scripts/test_validation.py`

## Troubleshooting
- **ImportError**: Make sure `$env:PYTHONPATH="."` is set.
- **Database Errors**: Delete `bookkeeping.db` and re-run migrations (`alembic upgrade head`) to start fresh.
