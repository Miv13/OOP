drop table if exists data;
create table data (
	id integer primary key autoincrement,
	px text not null,
	py text not null,
	pz text not null,
	vx text not null,
	vy text not null,
	vz text not null,
	force text not null,
	direction text not null,
	charge text not null,
	data_pub datetime not null

);

insert into data (id,px,py,pz,vx,vy,vz,force,direction,charge,data_pub)
values (null, '4', '4', '4', '5', '5', '5', '6', 'positive', 'proton', datetime(current_timestamp));
