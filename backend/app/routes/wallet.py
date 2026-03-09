
from fastapi import APIRouter
from ..wallet_engine import create_wallet

router = APIRouter(prefix="/wallet")

@router.get("/create")
def new_wallet():
    return create_wallet()
