from fastapi import APIRouter, HTTPException

from app.domain.services.seller_service import SellerService
from app.dtos.mapper import seller_to_schema
from app.dtos.seller_schema import SellerSchema
from app.infrastructure.data.seller_repository_json import SellerRepositoryJson
from app.shared.exceptions import ProductNotFoundException, SellerNotFoundException

router = APIRouter()

repository = SellerRepositoryJson("app/infrastructure/data/seller.json")
service = SellerService(repository)

@router.get("/by-product/{product_id}", response_model=SellerSchema)
def get_seller_by_product_id(product_id: str):
    try:
        seller = service.get_seller_by_product_id(product_id)
        return seller_to_schema(seller)
    except ProductNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SellerNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")