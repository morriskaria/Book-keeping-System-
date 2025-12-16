# MaturaCo Hospital Bookkeeping System

A comprehensive, secure, and scalable bookkeeping system designed for MaturaCo Hospital. This application manages patient billing, payments, staff payroll, inventory, and generates financial reports.

## Features
- **Authentication**: Secure login with Role-Based Access Control (Admin, Doctor, Cashier).
- **Billing**: Create invoices for patients and track partial payments.
- **Inventory**: Track drug levels and get low-stock alerts.
- **Payroll**: Manage staff salaries and payments.
- **Reports**: Real-time Profit & Loss statements.

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   ```bash
   alembic upgrade head
   ```

3. **Create Admin User**
   ```bash
   $env:PYTHONPATH="."
   python app/scripts/create_admin.py
   ```

4. **Run Server**
   ```bash
   uvicorn app.main:app --reload
   ```
   Open [http://localhost:8000/docs](http://localhost:8000/docs) to access the system.

## Documentation
- [User Manual](USER_MANUAL.md): Guide for Hospital Staff.
- [Testing Guide](TESTING.md): Guide for Developers.

## Technology Stack
- **Backend**: FastAPI (Python)
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
