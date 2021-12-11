drop table if exists game cascade;
create table game(
	game_id int primary key not null,
	season int not null,
	type_ varchar(20),
	date_time varchar(20),
	away_team_id int not null,
	home_team_id int not null,
	away_goals int, 
	home_goals int,
	outcome varchar(20)
);

drop table if exists game_plays cascade;
create table game_plays(
	play_id varchar(20) primary key not null,
	game_id int references game(game_id),
	team_id_for int not null,
	team_id_against int not null,
	event_ varchar(20),
	period_ int not null,
	periodType varchar(20),
	periodTime int
);

drop table if exists player_info cascade;
create table player_info(
	player_id int primary key not null,
	firstName varchar(20),
	lastName varchar(20),
	nationality varchar(20),
	primaryPosition varchar(20),
	birthDate date not null
);

drop table if exists game_plays_players;
create table game_plays_players(
	play_id varchar(20) references game_plays(play_id),
	player_id int not null references player_info(player_id),
	playerType varchar(20),
	primary key(play_id, player_id)
);

drop table if exists team_info cascade;
create table team_info(
	team_id int not null primary key,
	franchiseId int not null,
	shortName varchar(20),
	teamName varchar(20),
	abbreviation varchar(20),
	link_ varchar(20)
);


drop table if exists game_skater_stats;
create table game_skater_stats(
	game_id int not null references game(game_id),
	player_id int not null references player_info(player_id),
	team_id int not null references team_info(team_id),
	timeOnice int,
	assists int,
	goals int,
	shots int, 
	hits int, 
	takeaways int,
	giveaways int,
	constraint game_skater_stats_pk primary key (game_id, player_id, team_id)
);

drop table if exists game_goalie_stats;
create table game_goalie_stats(
	game_id int not null references game(game_id),
	player_id int not null references player_info(player_id),
	team_id int not null references team_info(team_id),
	timeOnice int,
	assists int,
	goals int,
	shots int, 
	hits int, 
	saves int,
	constraint game_goalie_stats_pk primary key (game_id, player_id, team_id)
);
