from pydantic import BaseModel
import datetime


class Match(BaseModel):
    id: int
    naverid: int
    sofascoredid: int
    home: str
    away: str
    starttime: datetime.datetime