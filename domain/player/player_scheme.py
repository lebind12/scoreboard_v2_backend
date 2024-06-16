from pydantic import BaseModel


class Player(BaseModel):
    id: int
    korname: str
    sofascoredid: str