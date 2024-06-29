from database import SessionLocal
from models import Match
import requests
import json
import pprint
db = SessionLocal()

# naver n강 데이터
KOREAN_NAVER_URL = "https://api-gw.sports.naver.com/schedule/games?fields=basic%2CsuperCategoryId%2CcategoryName%2Cstadium%2CstatusNum%2CgameOnAir%2ChasVideo%2Ctitle%2CspecialMatchInfo%2CroundCode%2CseriesOutcome%2CseriesGameNo%2CmatchRound%2CroundTournamentInfo%2CphaseCode%2CgroupName%2Cleg%2ChasPtSore%2ChomePtScore%2CawayPtScore%2Cleague%2CleagueName%2CaggregateWinner%2CneutralGround%2Cpostponed&upperCategoryId=wfootball&categoryId=uefaeuro&season=2024&phaseCode=T"
# 16강
ROUNDS = ["16", '8', '4', '2']
naver_home_name = []
naver_away_name = []
naver_stadium = []
naver_gameDatetime = []
naver_id = []

for round in ROUNDS:
    res = json.loads(requests.get(KOREAN_NAVER_URL + round).text)
    games = res['result']['games']
    for game in games:
        
        naver_home_name.append(game['homeTeamName'])
        naver_away_name.append(game['awayTeamName'])
        naver_stadium.append(game["stadium"])
        naver_gameDatetime.append(game['gameDateTime'])
        naver_id.append(game["gameId"])
        
# sofascored 데이터
SOFASCORED_URL = "https://www.sofascore.com/api/v1/unique-tournament/1/season/56953/events/next/0"
res = json.loads(requests.get(SOFASCORED_URL).text)
events = res['events']

sofa_homeid = []
sofa_awayid = []
sofa_homeCode = []
sofa_awayCode = []
sofa_gameid = []

for event in events:
    sofa_homeid.append(event['homeTeam']['id'])
    sofa_awayid.append(event['awayTeam']['id'])
    sofa_homeCode.append(event['homeTeam']['nameCode'])
    sofa_awayCode.append(event['awayTeam']['nameCode'])
    sofa_gameid.append(event['id'])
    
for i in range(len(sofa_homeid)):
    data = Match(naverid=naver_id[i], sofascoredid=sofa_gameid[i],
                 home=naver_home_name[i], away=naver_away_name[i],
                 homeid=int(sofa_homeid[i]), awayid=int(sofa_awayid[i]),
                 starttime=naver_gameDatetime[i],
                 homenamecode=str(sofa_homeCode[i]), awaynamecode=str(sofa_awayCode[i]),
                 matchstadium=naver_stadium[i])
    db.add(data)
    print(naver_id[i], sofa_gameid[i],
          naver_home_name[i],naver_away_name[i],
          sofa_homeid[i], sofa_awayid[i],
          naver_gameDatetime[i],
          sofa_homeCode[i], sofa_awayCode[i],
          naver_stadium[i])
    
db.commit()