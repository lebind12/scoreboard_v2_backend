from models import Match
from sqlalchemy.orm import Session
import requests, json


def get_match_detail(db: Session, match_id: int):
    db_match = db.query(Match).get(match_id)
    print(db_match.naverid)
    return db_match

def get_match_list(db: Session):
    db_match_list = db.query(Match).all()
    return db_match_list

def get_recent_comment(game_id: int):
    res = requests.get("https://api-gw.sports.naver.com/schedule/games/"+ str(game_id) +"/game-polling")
    return (json.loads(res.text)['result']['textRelayData'])