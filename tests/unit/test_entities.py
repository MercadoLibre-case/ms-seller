from app.domain.entities.seller import Seller, Products
from app.domain.services.seller_service import SellerService
from app.domain.interfaces.seller_repository_interface import ISellerRepository
from app.dtos.mapper import seller_to_schema
from app.dtos.seller_schema import SellerSchema

class FakeRepo(ISellerRepository):
    def get_seller_by_product_id(self, product_id: str):
        if product_id == "1":
            return Seller(
                id="seller123",
                name="Tech World",
                cover_image="cover.jpg",
                reputation=4.9,
                products=[Products(id="1", title="iPhone", image="img.jpg")]
            )
        return None

def test_products_entity():
    p = Products(id="1", title="iPhone", image="image.jpg")
    assert p.id == "1"
    assert p.title == "iPhone"
    assert p.image == "image.jpg"

def test_seller_entity():
    p = Products(id="1", title="iPhone", image="image.jpg")
    s = Seller(id="seller123", name="Tech World", cover_image="cover.jpg", reputation=4.5, products=[p])
    assert s.id == "seller123"
    assert s.name == "Tech World"
    assert s.reputation == 4.5
    assert len(s.products) == 1
    assert s.products[0].title == "iPhone"

def test_seller_service():
    service = SellerService(FakeRepo())
    seller = service.get_seller_by_product_id("1")
    assert seller.name == "Tech World"
    assert seller.products[0].id == "1"

def test_seller_mapper():
    seller = Seller(
        id="seller123",
        name="Tech World",
        cover_image="cover.jpg",
        reputation=4.9,
        products=[Products(id="1", title="iPhone", image="img.jpg")]
    )
    dto = seller_to_schema(seller)
    assert isinstance(dto, SellerSchema)
    assert dto.id == "seller123"
    assert dto.products[0].title == "iPhone"