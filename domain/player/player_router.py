from fastapi import APIRouter, Depends
from domain.player.player_scheme import Player
from domain.player.player_crud import get_sofascore_id
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(
    prefix="/api/player"
)

@router.get("/id")
def get_sofa_id(player_id: int, db: Session = Depends(get_db)):
    sofa_id = get_sofascore_id(db, player_id)
    if sofa_id == None:
        return {
            "id": -99,
            "korname": "Noname",
            "sofascoredid": player_id,
            "familyname" : "Noname"
        }
    else:
        return sofa_id