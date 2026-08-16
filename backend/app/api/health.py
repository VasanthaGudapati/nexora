from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Health check endpoint to verify that the Nexora backend server is running."""
    return {"status": "ok"}
