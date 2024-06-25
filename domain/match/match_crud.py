from models import Match, Player
from sqlalchemy.orm import Session
import requests, json
from pprint import pprint


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

def get_match_lineup(home_code:str, away_code:str, db: Session):
    result = {
        "type": "success",
        "home": {
            
        },
        "away": {
            
        }
    }
    try:
        home_lineup = db.query(Player).filter(Player.nation_code == home_code)
        away_lineup = db.query(Player).filter(Player.nation_code == away_code)
        
        
        
        for player in home_lineup:
            result["home"][player.sofascoredid] = player.familyname
        for player in away_lineup:
            result["away"][player.sofascoredid] = player.familyname
        return result
    except:
        return {
            "type": "error",
            "text": "No nation code in database"
        }