# Hospital Bookkeeping System - User Manual

Welcome to the MaturaCo Hospital Bookkeeping System. This guide will help you manage patients, invoices, payments, and hospital operations.

## 1. Getting Started
- **Access**: Open your web browser and navigate to the system URL (e.g., `http://localhost:8000/docs`).
- **Login**: Click the "Authorize" button (green lock) and enter your email and password.
    - *Default Admin*: `admin@matura.co` / `admin123`

## 2. For Receptionists (Patients)
**Goal**: Register new patients when they walk in.
1. Go to **Billing** -> `POST /billing/patients`.
2. Click **Try it out**.
3. Enter Name, Age, and Phone.
4. Click **Execute**.
5. Note the `id` of the new patient.

## 3. For Doctors/Cashiers (Billing)
**Goal**: Create a bill for a patient.
1. **Create Invoice**: Go to `POST /billing/invoices`.
    - Enter `patient_id`.
    - Add items (Services) by `service_id` and `quantity`.
2. **View Invoice**: Go to `GET /billing/invoices/{id}` to see the total amount.

## 4. For Cashiers (Payments)
**Goal**: Receive money from a patient.
1. Go to `POST /billing/payments`.
2. Enter the `invoice_id` and the `amount` paid.
3. Select Method: `cash`, `card`, `mpesa`, or `insurance`.
4. **Note**: If they pay the full amount, the invoice status changes to `PAID`.

## 5. For Admins (Staff & Reports)
### Managing Staff (Payroll)
- **Hire**: `POST /payroll/staff`.
- **Pay**: `POST /payroll/payroll` to record salary payments.

### Tracking Inventory
- **Check Low Stock**: `GET /inventory/low-stock`.
- **Restock**: `POST /inventory/{id}/restock`.

### Financial Reports
- **View Profit/Loss**: `GET /reports/summary`.
- You can filter by dates to see "This Month" or "Today".

## 6. Managing Expenses
**Goal**: Record hospital costs (buying supplies, paying electricity).
1. Go to `POST /expenses/`.
2. Enter the Title (e.g., "Electricity"), Amount, and Category (`utilities`, `medical_supplies`).

---
**Need Help?**
Contact the IT Department for password resets or technical issues.
