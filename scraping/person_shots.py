import numpy as np
import pandas as pd
from matplotlib import pyplot
import json
# import nba_api
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import teams, players

l = players.find_players_by_first_name("LeBron")
print(l)
z = teams.find_teams_by_nickname("LAL")
print(z)


res = shotchartdetail.ShotChartDetail(0, 2544)
content = json.loads(res.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers

df.to_csv("f.csv", index=False)



custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}