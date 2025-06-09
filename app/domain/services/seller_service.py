from app.domain.entities.seller import Seller
from app.domain.interfaces.seller_repository_interface import ISellerRepository
from app.shared.exceptions import SellerNotFoundException


class SellerService:
    def __init__(self, repository: ISellerRepository):
        self.repository = repository

    def get_seller_by_product_id(self, product_id: str) -> Seller:
        seller =self.repository.get_seller_by_product_id(product_id)
        if not seller:
            raise SellerNotFoundException()
        return seller