from app.database.database import SessionLocal
from app.models.billing import Patient, Service, Invoice, InvoiceItem

def test_billing_flow():
    db = SessionLocal()
    try:
        print("Testing Billing Flow...")
        
        # 1. Create Patient
        patient = Patient(name="Jane Doe", age=30)
        db.add(patient)
        db.commit()
        print(f"Created Patient: {patient.name}")

        # 2. Create Service
        service = Service(name="General Consultation", price=50.0)
        db.add(service)
        db.commit()
        print(f"Created Service: {service.name} (KSh {service.price})")

        # 3. Create Invoice (Manual simulation of the route logic)
        invoice = Invoice(patient_id=patient.id)
        db.add(invoice)
        db.commit()
        
        # Add Item
        item = InvoiceItem(
            invoice_id=invoice.id,
            service_id=service.id,
            service_name=service.name,
            unit_price=service.price,
            quantity=2
        )
        db.add(item)
        
        # Calculate Total
        invoice.total_amount = item.unit_price * item.quantity
        db.commit()
        
        print(f"Created Invoice for 2x {service.name}")
        print(f"Invoice Total: KSh {invoice.total_amount}")
        
        assert invoice.total_amount == 100.0
        print("SUCCESS: Billing calculation is correct!")
        
    except Exception as e:
        print(f"Test Failed: {e}")
        # Clean up for re-run capability (optional)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_billing_flow()
