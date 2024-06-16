from models import Player
from sqlalchemy.orm import Session


def get_sofascore_id(db: Session, player_id: int):
    db_sofaId = db.query(Player).filter(Player.sofascoredid == player_id).first()
    return db_sofaId