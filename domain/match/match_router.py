from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domain.match.match_crud import get_match_detail, get_match_list, get_recent_comment, get_match_lineup
from domain.match.match_scheme import Match
from models import Match
from database import get_db


router = APIRouter(
    prefix="/api/match"
)

@router.get("/id")
def get_match(match_id: int, db: Session = Depends(get_db)):
    match = get_match_detail(db, match_id)
    return match

@router.get("/list")
def get_every_match(db: Session = Depends(get_db)):
    list = get_match_list(db)
    return list

@router.get("/comment")
def get_match(match_id: int):
    comment = get_recent_comment(match_id)
    return comment

@router.get("/lineup")
def get_lineup(home_code:str, away_code:str, db: Session = Depends(get_db)):
    lineup = get_match_lineup(home_code, away_code, db)
    return lineup