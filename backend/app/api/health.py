from fastapi import APIRouter

router = APIRouter()

# Health check endpoint
@router.get("/health")
def health_check():
    """Health check endpoint to verify that the Nexora backend server is running."""
    return {"status": "ok"}
