drop table if exists team_info_copy;
create table team_info_copy as select * from team_info;
delete from team_info_copy;


do $$
declare
	team_id team_info_copy.team_id%TYPE;
	franchiseid team_info_copy.franchiseid%TYPE;
	shortname team_info_copy.shortname%TYPE;
	abbreviation team_info_copy.abbreviation%TYPE;

begin
	team_id:=1;
	franchiseid:=23;
	shortname:='New Jersey';
	abbreviation:='NJD';
	
	for counter in 1..10
		loop
			insert into team_info_copy(team_id, franchiseid, shortname, abbreviation)
			values(team_id+counter, franchiseid+counter, shortname || counter, abbreviation || counter);
		end loop;
end;
$$