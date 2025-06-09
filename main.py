from fastapi import FastAPI
from app.controllers.seller_controller import router as product_router

app = FastAPI(title="Seller Detail Microservice")

app.include_router(product_router, prefix="/sellers")
