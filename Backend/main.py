from fastapi import FastAPI # Import the FastAPI class from the fastapi module.

# Create the FastAPI instance. This is the main entry point.
# title, description, and version will appear in the automatic /docs API documentation.
app = FastAPI(
    title="Hospital Bookkeeping System",
    description="A comprehensive system for managing hospital finances including billing, expenses, and payroll.",
    version="1.0.0"
)

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
