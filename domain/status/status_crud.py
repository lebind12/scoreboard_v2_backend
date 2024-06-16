from models import Player
from sqlalchemy.orm import Session
import requests
import json


SOFA_URL = "https://www.sofascore.com/api/v1/event/{}/player/{}/statistics"
def get_sofascore_id(db: Session, player_id: int, match_id: int):
    db_sofaId = db.query(Player).get(player_id)
    sofa_player_id = db_sofaId.sofascoredid
    print(SOFA_URL.format(str(match_id), str(sofa_player_id)))
    res = requests.get(SOFA_URL.format(str(match_id), str(sofa_player_id)))
    
    try:
        result = json.loads(res.text)['statistics']
        print(json.loads(res.text)['statistics'])
        return result
    except:
        print(json.loads(res.text))
        return