from app.schemas.billing import PaymentCreate, PaymentMethod
from pydantic import ValidationError

def test_validation_logic():
    try:
        print("Testing Validation Logic...")
        
        # 1. Try Negative Payment
        print("Attempting to create Payment with -100...")
        try:
            PaymentCreate(
                invoice_id=1,
                amount=-100.0,
                payment_method=PaymentMethod.CASH
            )
            print("FAILURE: Validation DID NOT catch negative amount!")
        except ValidationError as e:
            print("SUCCESS: Caught expected validation error:")
            print(e)
            
        # 2. Try Zero Payment (if restricted to >0)
        print("\nAttempting to create Payment with 0...")
        try:
            PaymentCreate(
                invoice_id=1,
                amount=0.0,
                payment_method=PaymentMethod.CASH
            )
            print("FAILURE: Validation DID NOT catch zero amount!")
        except ValidationError as e:
            print("SUCCESS: Caught expected validation error for zero.")

    except Exception as e:
        print(f"Test Failed: {e}")

if __name__ == "__main__":
    test_validation_logic()
