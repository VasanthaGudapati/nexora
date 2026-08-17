from fastapi import FastAPI

from backend.app.api.customers import router as customer_router
from backend.app.api.health import router as health_router

app = FastAPI(
    title="Nexora API",
    description="Business Intelligence & Analytics Engine",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(customer_router)
