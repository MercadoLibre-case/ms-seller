import json
from pathlib import Path
from typing import List

from app.domain.entities.seller import Seller
from app.domain.interfaces.seller_repository_interface import ISellerRepository
from app.dtos.mapper import dict_to_seller


class SellerRepositoryJson(ISellerRepository):
    def __init__(self, data_file: str):
        self.data_file = Path(data_file)

    def _load_data(self) -> List[dict]:
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_seller_by_product_id(self, product_id: str) -> Seller | None:
        data = self._load_data()
        for s in data:
            if any(p["id"] == product_id for p in s.get("products", [])):
                return dict_to_seller(s)
        return None
