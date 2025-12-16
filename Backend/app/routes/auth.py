from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import database
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Token
from app.core import security

router = APIRouter()

# This tells FastAPI that we use "Bearer Tokens" for security.
# The URL "/auth/login" is where clients get the token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(database.get_db)):
    """
    Register a new user.
    """
    # 1. Check if email already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password
    hashed_password = security.get_password_hash(user.password)
    
    # 3. Create the user object
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    
    # 4. Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    """
    Get an access token (Login).
    Users send 'username' (email) and 'password'.
    """
    # 1. Find user by email
    user = db.query(User).filter(User.email == form_data.username).first()
    
    # 2. Check password
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Create Token
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email, "role": user.role.value}, # We store role in token too!
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
