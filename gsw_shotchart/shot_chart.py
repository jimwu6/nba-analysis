import numpy as np
import pandas as pd 
import json

#import nba api
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import teams, players

nba_teams = teams.get_teams()
gsw = [team for team in nba_teams if team['abbreviation'] == 'GSW'][0]
gsw_id = gsw['id']

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=gsw_id)
games = gamefinder.get_data_frames()[0]
games.head()

gsw_shotchart = shotchartdetail.ShotChartDetail(team_id=gsw_id, player_id=0, season_nullable="2017-18")
gsw_shotchart_json = json.loads(gsw_shotchart.get_json())

results = gsw_shotchart_json['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers
df.to_csv("gsw.csv", index=None)