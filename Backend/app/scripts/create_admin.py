from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.core.security import get_password_hash

def create_admin_user():
    db = SessionLocal()
    try:
        # Check if admin already exists
        user = db.query(User).filter(User.email == "admin@matura.co").first()
        if user:
            print("Admin user already exists.")
            return

        # Create new admin
        admin_user = User(
            email="admin@matura.co",
            hashed_password=get_password_hash("admin123"),
            role=UserRole.ADMIN,
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        print("Admin user created successfully!")
        print("Email: admin@matura.co")
        print("Password: admin123")
    except Exception as e:
        print(f"Error creating admin: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin_user()
