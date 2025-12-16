from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, billing, expenses, payroll, inventory, reports

# Create the FastAPI instance. This is the main entry point.
# title, description, and version will appear in the automatic /docs API documentation.
app = FastAPI(
    title="Hospital Bookkeeping System",
    description="A comprehensive system for managing hospital finances including billing, expenses, and payroll.",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for dev, or specific ports like ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connect the auth routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(billing.router, prefix="/billing", tags=["Billing"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
app.include_router(payroll.router, prefix="/payroll", tags=["Payroll"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])

# Define a route handling GET requests at the "/health" path.
# This is a standard practice to check if the server is up and running.
@app.get("/health")
def health_check():
    """
    Health Check Endpoint
    Returns the status of the API to verify it is running correctly.
    """
    # Return a Python dictionary, which FastAPI automatically converts to JSON.
    return {"status": "ok"}
