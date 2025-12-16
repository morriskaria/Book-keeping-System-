from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Create the SQLAlchemy Engine
# The engine is the central point of contact with your database.
# connect_args={"check_same_thread": False} is needed ONLY for SQLite.
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# 2. Create the SessionLocal class
# Each instance of this class will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create the Base class
# Later, we will inherit from this class to create our Database Models.
Base = declarative_base()

# 4. Dependency
# This helper function will be used in our API routes to get a database session.
# It ensures the session is closed after the request is finished.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
