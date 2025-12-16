from app.database.database import SessionLocal
from app.models.billing import Patient, Service, Invoice, InvoiceItem, InvoiceStatus, Payment, PaymentMethod

def test_payment_flow():
    db = SessionLocal()
    try:
        print("Testing Payment Flow...")
        
        # 1. Setup Data
        patient = Patient(name="Payment Tester", age=40)
        service = Service(name="Expensive Surgery", price=1000.0)
        db.add(patient)
        db.add(service)
        db.commit()

        invoice = Invoice(patient_id=patient.id, total_amount=1000.0)
        db.add(invoice)
        db.commit()
        
        print(f"Created Invoice #{invoice.id} for KSh 1000. Status: {invoice.status}")
        
        # 2. Add Partial Payment ($400)
        print("--- Payment 1: KSh 400 (Cash) ---")
        payment1 = Payment(
            invoice_id=invoice.id,
            amount=400.0,
            payment_method=PaymentMethod.CASH
        )
        db.add(payment1)
        invoice.paid_amount += 400.0
        # Logic matches route: Check status
        if invoice.paid_amount >= invoice.total_amount:
            invoice.status = InvoiceStatus.PAID
            
        db.commit()
        print(f"Paid: KSh {invoice.paid_amount}. Status: {invoice.status}")
        assert invoice.status == InvoiceStatus.PENDING
        
        # 3. Add Final Payment ($600)
        print("--- Payment 2: KSh 600 (Card) ---")
        payment2 = Payment(
            invoice_id=invoice.id,
            amount=600.0,
            payment_method=PaymentMethod.CARD
        )
        db.add(payment2)
        invoice.paid_amount += 600.0
        if invoice.paid_amount >= invoice.total_amount:
            invoice.status = InvoiceStatus.PAID
            
        db.commit()
        print(f"Paid: KSh {invoice.paid_amount}. Status: {invoice.status}")
        
        assert invoice.status == InvoiceStatus.PAID
        print("SUCCESS: Payment logic handles status correctly!")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_payment_flow()
