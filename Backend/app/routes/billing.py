from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import database
from app.models.billing import Patient, Service, Invoice, InvoiceItem, InvoiceStatus
from app.schemas.billing import PatientCreate, PatientResponse, ServiceCreate, ServiceResponse, InvoiceCreate, InvoiceResponse

router = APIRouter()

# --- PATIENTS ---
@router.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(database.get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/patients", response_model=List[PatientResponse])
def get_patients(db: Session = Depends(database.get_db)):
    return db.query(Patient).all()

# --- SERVICES ---
@router.post("/services", response_model=ServiceResponse)
def create_service(service: ServiceCreate, db: Session = Depends(database.get_db)):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

@router.get("/services", response_model=List[ServiceResponse])
def get_services(db: Session = Depends(database.get_db)):
    return db.query(Service).all()

# --- INVOICES ---
@router.post("/invoices", response_model=InvoiceResponse)
def create_invoice(invoice_data: InvoiceCreate, db: Session = Depends(database.get_db)):
    # 1. Check Patient exists
    patient = db.query(Patient).filter(Patient.id == invoice_data.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    # 2. Create Invoice (initially 0 total)
    new_invoice = Invoice(
        patient_id=invoice_data.patient_id,
        status=InvoiceStatus.PENDING,
        total_amount=0.0
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)

    total = 0.0

    # 3. Add Items & Calculate Total
    for item in invoice_data.items:
        service = db.query(Service).filter(Service.id == item.service_id).first()
        if not service:
            continue # Or raise error
        
        # Snapshot the price
        inv_item = InvoiceItem(
            invoice_id=new_invoice.id,
            service_id=service.id,
            service_name=service.name,
            unit_price=service.price,
            quantity=item.quantity
        )
        db.add(inv_item)
        total += (service.price * item.quantity)
    
    # 4. Update Invoice Total
    new_invoice.total_amount = total
    db.commit()
    db.refresh(new_invoice)
    
    return new_invoice

@router.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: int, db: Session = Depends(database.get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

# --- PAYMENTS ---
from app.models.billing import Payment, PaymentMethod
from app.schemas.billing import PaymentCreate, PaymentResponse

@router.post("/payments", response_model=PaymentResponse)
def create_payment(payment_data: PaymentCreate, db: Session = Depends(database.get_db)):
    # 1. Get Invoice
    invoice = db.query(Invoice).filter(Invoice.id == payment_data.invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    # 2. Create Payment Record
    new_payment = Payment(
        invoice_id=invoice.id,
        amount=payment_data.amount,
        payment_method=payment_data.payment_method,
        transaction_id=payment_data.transaction_id
    )
    db.add(new_payment)
    
    # 3. Update Invoice Paid Amount
    invoice.paid_amount += payment_data.amount
    
    # 4. Update Status if fully paid
    # Use a small epsilon for float comparison safety, or just >=
    if invoice.paid_amount >= invoice.total_amount:
        invoice.status = InvoiceStatus.PAID
    
    db.commit()
    db.refresh(new_payment)
    
    return new_payment
