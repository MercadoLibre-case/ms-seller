from abc import ABC, abstractmethod

from app.domain.entities.seller import Seller


class ISellerRepository(ABC):

    @abstractmethod
    def get_seller_by_product_id(self, product_id: str) -> Seller | None:
        pass
