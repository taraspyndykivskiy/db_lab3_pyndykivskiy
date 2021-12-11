import psycopg2
import math
import matplotlib.pyplot as plt

username = 'taras_pyndykivskiy'
password = 'taras_pyndykivskiy'
database = 'second_lab'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE view players_types as
select playerType, count(*) from game_plays_players group by playerType;
'''

query_2='''
CREATE view teams_goals as
SELECT abbreviation, sum(away_goals) as goals from team_info join game on game.away_team_id=team_info.team_id
group by abbreviation;
'''

query_3 = '''
CREATE view shots_goals_relationship as
SELECT game.home_goals, sum(game_skater_stats.shots) as home_overall_shots from game join game_skater_stats on game.game_id=game_skater_stats.game_id
group by game.home_goals
order by sum(game_skater_stats.shots) asc;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur=conn.cursor()

    cur.execute('DROP view if exists players_types')

    cur.execute(query_1)

    cur.execute('select * from players_types')

    player_type=[]
    players_quantity=[]

    for row in cur:
        player_type.append(row[0])
        players_quantity.append(row[1])

    x_range=range(len(player_type))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar = bar_ax.bar(x_range, players_quantity, label='Total')
    bar_ax.set_title('Кількість відіграних ролей за частину гри')
    bar_ax.set_xlabel('Ролі')
    bar_ax.set_ylabel('Кількість появ')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(player_type)


    cur.execute('drop view if exists teams_goals')

    cur.execute(query_2)

    cur.execute('select * from teams_goals')

    team_name=[]
    away_goals=[]

    for row in cur:
        team_name.append(row[0])
        away_goals.append(row[1])

    pie_ax.pie(away_goals, labels=team_name, autopct='%1.1f%%')
    pie_ax.set_title('Частка кількостей забитих голів командами')


    cur.execute('drop view if exists shots_goals_relationship')

    cur.execute(query_3)

    cur.execute('select * from shots_goals_relationship')
    
    goals = []
    shots = []
  
    for row in cur:
        shots.append(row[0])
        goals.append(row[1])

    graph_ax.plot(goals, shots, marker='o')

    graph_ax.set_xlabel('Кількість кидків')
    graph_ax.set_ylabel('Кількість голів')
    graph_ax.set_title('Графік залежності кількості голів від числа кидків')

    for shts, gls in zip(shots, goals):
        graph_ax.annotate(shts, xy=(shts, gls), xytext=(7, 2), textcoords='offset points')    


mng = plt.get_current_fig_manager()
mng.resize(1600, 800)

plt.show()    