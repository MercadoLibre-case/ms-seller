from typing import List


class Products:
    def __init__(self,
                 id: str,
                 title: str,
                 image: str):
        self.id = id
        self.title = title
        self.image = image

class Seller:
    def __init__(self,
                 id: str,
                 name: str,
                 cover_image: str,
                 reputation: float,
                 products: List[Products]):
        self.id = id
        self.name = name
        self.cover_image = cover_image
        self.reputation = reputation
        self.products = products
