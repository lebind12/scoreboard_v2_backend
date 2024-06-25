from models import Match, Player
from database import SessionLocal
from datetime import datetime
import requests
import json
from pprint import pprint
from datetime import datetime
from bs4 import BeautifulSoup
import time
from urllib import parse


# def get_date(isoformatdate:str) -> str:
#     year, month, day = (isoformatdate.split('T')[0].split('-'))
#     hour, minute, second = isoformatdate.split('T')[1].split(':')
#     return year + month + day + hour + minute
# def make_datetime(date:str) -> datetime:
#     year = int(date[:4])
#     month = int(date[4:6])
#     day = int(date[6:8])
#     hour = int(date[8:10])
#     minute = int(date[10:])
#     return datetime(year, month, day, hour, minute)

# # 경기 날짜 YYYYMMDD
# match_date = ['20240615', '20240701', '20240622', '20240619', '20240702', '20240620', '20240706', '20240710', '20240627', '20240624', '20240630', '20240707', '20240625', '20240618', '20240715', '20240623', '20240617', '20240616', '20240621', '20240711', '20240626', '20240703']
# nation_id = [4481, 4484, 4763, 4690, 6355, 4695, 4697, 4698, 4699, 4700, 4701, 4703, 4704, 4705, 4707, 4709, 4711, 4713, 4714, 4715, 4717, 4718, 4476, 4477]

# # TODO
# # Sofascore 데이터 수집
# result_data = {
#     0: [11873905,
#      datetime(2024, 6, 15, 19, 00),
#      'Germany',
#      'scotland',
#      4711,
#      4695]
# }
# id = 1

# # Sofascore
# EVENT_URL = "https://www.sofascore.com/api/v1/unique-tournament/1/season/56953/events/next/"
# NAVER_URL = "https://sports.news.naver.com/wfootball/ajax/templateMatchBox.nhn?date="
# for i in range(2):
#     # 2 페이지 있음
#     res = requests.get(EVENT_URL + str(i))
#     events = json.loads(res.text)['events']
#     # pprint(json.loads(res.text)['events'])
#     for event in events:
        
#         # pprint(event['id'])
#         # pprint(event['startTimestamp'])
#         # pprint(event['homeTeam']['name'])
#         # pprint(event['awayTeam']['name'])
#         value = datetime.fromtimestamp(int(event['startTimestamp'])).isoformat()
#         # print(get_date(value))
#         result_data[id] = [event['id'], make_datetime(get_date(value)), event['homeTeam']['name'], event['awayTeam']['name'], event['homeTeam']['id'], event['awayTeam']['id']]
#         id += 1
# # pprint(result_data)
#     # 가져와야할 것 id, startTimestamp
# id = 0
# # Naver
# match_date = sorted(list(set(match_date)))
# # print(match_date)
# for date in match_date:
#     naver_url = NAVER_URL + date
#     # print(naver_url)
#     res = requests.get(naver_url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     value = soup.select(selector="#_tab_box_uefaeuro > div > ul")
    
#     for v in value:
#         naver_id_list = list(v.select("li > div.btn_wrap > a"))
#         home_list = list(v.select("li > div.vs_list.vs_list1 > div > span.name"))
#         away_list = list(v.select("li > div.vs_list.vs_list2 > div > span.name"))
#         for i in range(len(naver_id_list)):
#             naver_id, home, away = naver_id_list[i].get('href').split('/')[-1], home_list[i].get_text(), away_list[i].get_text()
#             # print(naver_id, home, away)
#             result_data[id] += [naver_id, home, away]
#             id += 1
            
# # pprint(result_data)
# db = SessionLocal()
# for id in result_data:
#     data=result_data[id]
#     m = Match(id=id, naverid=data[6], sofascoredid=data[0], home=data[7], away=data[8], homeid=data[4], awayid=data[5], starttime=data[1])
#     db.add(m)
# db.commit()
# sofascore player id
# PLAYER_URL = "https://www.sofascore.com/api/v1/team/"
# for nid in nation_id:
#     url = PLAYER_URL + str(nid) + "/players"
#     res = json.loads(requests.get(url).text)['players']
#     # print(res)    

# RADAR_URL = "https://api.sportradar.com/soccer/trial/v4/ko/competitors/"
# RADAR_BACK_URL = "/profile.json?api_key=IJrRAGrXzo8KGRWcSPL9F7gwpj4sJFpP9Howllis"
# competitor_id = ['sr:competitor:4711','sr:competitor:4695', 'sr:competitor:4699', 'sr:competitor:4709',
#                  'sr:competitor:4707', 'sr:competitor:4698', 'sr:competitor:4715', 'sr:competitor:4690',
#                  'sr:competitor:4713', 'sr:competitor:4484', 'sr:competitor:4476', 'sr:competitor:6355',
#                  'sr:competitor:4718', 'sr:competitor:4703', 'sr:competitor:4705', 'sr:competitor:4481',
#                  'sr:competitor:4701', 'sr:competitor:4477', 'sr:competitor:4717', 'sr:competitor:4697',
#                  'sr:competitor:4714', 'sr:competitor:4763', 'sr:competitor:4704', 'sr:competitor:4700']

# player_id = []
# player_en_ko = {}
# for comp_id in competitor_id[7:]:
#     res = requests.get(RADAR_URL + comp_id + RADAR_BACK_URL)
#     flag = comp_id + " SUCCESS"
#     try:
#         players = json.loads(res.text)['players']
#         print("Players length: " + str(len(players)))
#         for player in players:
#             player_id.append(player['id'])
#             # print(player_id)
#     except:
#         print(json.loads(res.text))
#         flag = comp_id + " Failed"
#     print(flag)
#     time.sleep(1)
    
# print(player_id)
# print(len(player_id))
    
# EN_RADAR_URL = "https://api.sportradar.com/soccer/trial/v4/en/players/"
# KO_RADAR_URL = "https://api.sportradar.com/soccer/trial/v4/ko/players/"
# RADAR_BACK_URL = "/profile.json?api_key=gKNDjFaoAZ8ga9xZDXZD93JMfLZA5hvW8fzFIly5"

# for pid in player_id:
#     try: 
#         en_res = requests.get(EN_RADAR_URL + pid + RADAR_BACK_URL)
#         # print(json.loads(en_res.text))
#         en_player = json.loads(en_res.text)['player']['name']
#         time.sleep(1)
#         ko_res = requests.get(KO_RADAR_URL + pid + RADAR_BACK_URL)
#         ko_player = json.loads(ko_res.text)['player']['name']
#         player_en_ko[en_player] = ko_player
#         time.sleep(1)
#         # print(player_en_ko)
#         print(f"{en_player}: {ko_player}")
#         with open('player_en_ko.txt', 'a') as f:
#             f.write(f"{en_player}: {ko_player}\n")
#     except:
#         print(json.loads(en_res.text))
#         print(json.loads(ko_res.text))
        
# # sr:player:1985243

# url = "https://www.sofascore.com/api/v1/search/all?q="
# with open('player_en_ko.txt', 'r') as f:
#     en_name, ko_name = f.readline().split(': ')
    
#     en_name = en_name.replace(',', '%2C')
#     en_name = en_name.replace(' ', '%20')
#     en_name = en_name.lower()
#     # print(url + en_name + "&page=0")
#     # res = requests.get(url + en_name + "&page=0")
#     res = requests.get("https://www.sofascore.com/api/v1/search/player-team-persons?q=Neuer%2C%20Manuel&page=0")
#     print(json.loads(res.text))
#     # try:
#     #     answer = json.loads(res.text)['results'][0]['entity']
#     #     print(answer['id'], answer['slug'])
#     # except:
#     #     print(json.loads(res.text))

# url = "https://www.sofascore.com/api/v1/search/player-team-persons"
# params = {
#     "q": "manuel-neuer",
#     "page": 0
# }

# res = requests.get(url, params=params)
# print(json.loads(res.text))

# db = SessionLocal()
# with open('player_en_ko_id.txt', 'r')as f:
#     lines = f.readlines()
#     id = 0
#     for line in lines:
#         en_name, ko_name, sofa_id = line.split("//")
#         sofa_id = int(sofa_id)
#         names = ko_name.split(",")
#         if len(names) > 1:
#             q = Player(id=id, korname=ko_name, sofascoredid=sofa_id, familyname=names[0].strip())
#             db.add(q)
#         else:
#             names = ko_name.split(' ')
#             if len(names) > 1:
#                 q = Player(id=id, korname=ko_name, sofascoredid=sofa_id, familyname=" ".join(names[1:]))
#             else:
#                 q = Player(id=id, korname=ko_name, sofascoredid=sofa_id, familyname=ko_name)
#             db.add(q)
#         id += 1
# db.commit()
# db.close()

