from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domain.status.status_crud import get_sofascore_id
from database import get_db


router = APIRouter(
    prefix="/api/status"
)

@router.get("/info")
def get_player_detail(player_id: int, match_id:int, db: Session = Depends(get_db)):
    player_detail = get_sofascore_id(db, player_id, match_id)
    return player_detail