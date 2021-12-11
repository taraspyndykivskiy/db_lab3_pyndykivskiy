import json
import psycopg2

username = 'taras_pyndykivskiy'
password = 'taras_pyndykivskiy'
database = 'second_lab'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:

    cur = conn.cursor()
    
    for table in ( 'game', 'game_goalie_stats', 'game_plays', 'game_plays_players', 'game_skater_stats', 'player_info', 'team_info'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default = str)
    