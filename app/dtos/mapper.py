from app.domain.entities.seller import Seller, Products
from app.dtos.seller_schema import SellerSchema, ProductsSchema


def seller_to_schema(seller: Seller) -> SellerSchema:
    return SellerSchema(
        id=seller.id,
        name=seller.name,
        cover_image=seller.cover_image,
        reputation=seller.reputation,
        products=[
            ProductsSchema(
                id=p.id,
                title=p.title,
                image=p.image
            )
            for p in seller.products
        ]
    )


def dict_to_seller(data: dict) -> Seller:
    return Seller(
        id=data["id"],
        name=data["name"],
        cover_image=data["cover_image"],
        reputation=data["reputation"],
        products=[
            Products(
                id=p["id"],
                title=p["title"],
                image=p["image"]
            )
            for p in data.get("products", [])
        ]
    )
