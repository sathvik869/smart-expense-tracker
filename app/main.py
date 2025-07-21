from fastapi import FastAPI
from app.routers import user

app = FastAPI(
    title="Smart Expense Tracker API",
    description="Track expenses and manage users",
    version="1.0.0"
)

# Include user routes
app.include_router(user.router)

