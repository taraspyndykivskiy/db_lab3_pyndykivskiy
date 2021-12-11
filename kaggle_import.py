import csv
import decimal
import psycopg2

username = 'taras_pyndykivskiy'
password = 'taras_pyndykivskiy'
database = 'second_lab'


INPUT_CSV_FILE = 'player_info.csv'

query_0 = '''
CREATE table player_info_new(
    player_id int primary key not null,
    firstName varchar(20),
    lastName varchar(20),
    nationality varchar(20),
    primaryPosition varchar(20),
    birthDate date not null
);

'''

query_1 = '''
DELETE FROM player_info_new
'''

query_2 = '''
INSERT INTO player_info_new (player_id, firstName, lastName, nationality, primaryPosition, birthDate) VALUES (%s, %s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute('drop table if exists player_info_new')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            plr_id = int(row['player_id'])
            values = (plr_id, row['firstName'], row['lastName'], row['nationality'], row['primaryPosition'], row['birthDate']) 
            cur.execute(query_2, values)

    conn.commit()
