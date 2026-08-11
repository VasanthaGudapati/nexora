from fastapi import FastAPI

app = FastAPI(
    title="Nexora API",
    description="Business Intelligence & Analytics Engine",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    """Health check endpoint to verify that the Nexora backend server is running."""
    return {"status": "ok"}
