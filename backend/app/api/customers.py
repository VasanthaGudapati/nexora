from fastapi import APIRouter, status

from backend.app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter(prefix="/api/v1", tags=["Customers"])

# In-memory customer storage
customers_db: list[dict] = []


@router.post("/customers", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate):
    """Create a new customer and store it in memory."""
    new_id = len(customers_db) + 1
    new_customer = {
        "id": new_id,
        "name": customer.name,
        "email": customer.email,
    }
    customers_db.append(new_customer)
    return new_customer


@router.get("/customers", response_model=list[CustomerResponse])
def get_customers():
    """Retrieve all stored customers."""
    return customers_db
