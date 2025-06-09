from typing import List

from pydantic import BaseModel


class ProductsSchema(BaseModel):
    id: str
    title: str
    image: str


class SellerSchema(BaseModel):
    id: str
    name: str
    cover_image: str
    reputation: float
    products: List[ProductsSchema]
