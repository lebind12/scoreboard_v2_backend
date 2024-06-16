from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.match import match_router
from domain.player import player_router
from domain.status import status_router


app = FastAPI()

origins = [
    "*",
    "http://localhost:3000",
    "https://scoreboard-v2-nine.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(match_router.router)
app.include_router(player_router.router)
app.include_router(status_router.router)