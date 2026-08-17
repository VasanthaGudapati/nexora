from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    email: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
