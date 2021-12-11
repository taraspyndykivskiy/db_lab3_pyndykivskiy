import csv
import psycopg2

username = 'taras_pyndykivskiy'
password = 'taras_pyndykivskiy'
database = 'second_lab'

OUTPUT_FILE_T = 'pyndykivskiy_DB_{}.csv'

TABLES = [
    'game',
    'game_goalie_stats',
    'game_plays',
    'game_plays_players',
    'game_skater_stats',
    'player_info',
    'team_info'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])

 
