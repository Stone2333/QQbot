create table Overview(
id int auto_increment primary key,
name varchar(30) not null unique,
SCORE_MIN  varchar(20) null,
KD_RATIO varchar(50) null,
WIN_PERCENT varchar(20) null,
KILLS_GAME varchar(20) null,
KILLS_MIN varchar(20) null,
INFANTRY_KPM varchar(20) null,
INFANTRY_KD varchar(20) null,
VEHICLE_KILLS varchar(20) null,
VEHICLE_KPM varchar(20) null,
SKILL varchar(20) null,
ACCURACY varchar(20) null,
INDEX(name)
)ENGINE=INNODB charset=utf8;


create table Recent_Sessions(
id int auto_increment primary key,
name varchar(30) not null unique,
SPM varchar(20) null,
KD varchar(20) null,
KPM varchar(20) null,
TimePlayed varchar(20) null,
SPM1 varchar(20) null,
KD1 varchar(20) null,
KPM1 varchar(20) null,
TimePlayed1 varchar(20) null,
SPM2 varchar(20) null,
KD2 varchar(20) null,
KPM2 varchar(20) null,
TimePlayed2 varchar(20) null,
INDEX(name)
)ENGINE=INNODB charset=utf8;


create table Server_id(
id int auto_increment primary key,
ServerName varchar(100) not null unique,
ServerID varchar(20) not null unique,
INDEX(ServerName,ServerID)
)ENGINE=INNODB charset=utf8;


create table Vehicles(
id int auto_increment primary key,
name varchar(30) not null unique,
VehiclesName varchar(100) null,
KILLS varchar(20) null,
KPM varchar(20) null,
Destroyed varchar(20) null,
VehiclesName1 varchar(100) null,
KILLS1 varchar(20) null,
KPM1 varchar(20) null,
Destroyed1 varchar(20) null,
VehiclesName2 varchar(100) null,
KILLS2 varchar(20) null,
KPM2 varchar(20) null,
Destroyed2 varchar(20) null,
INDEX(name)
)ENGINE=INNODB charset=utf8;


create table Weapons(
id int auto_increment primary key,
name varchar(30) not null unique,
WeaponsName varchar(100) null,
KILLS varchar(20) null,
KPM varchar(20) null,
Accuracy varchar(20) null,
Headshots varchar(20) null,
WeaponsName1 varchar(100) null,
KILLS1 varchar(20) null,
KPM1 varchar(20) null,
Accuracy1 varchar(20) null,
Headshots1 varchar(20) null,
WeaponsName2 varchar(100) null,
KILLS2 varchar(20) null,
KPM2 varchar(20) null,
Accuracy2 varchar(20) null,
Headshots2 varchar(20) null,
INDEX(name)
)ENGINE=INNODB charset=utf8;


create table user(
id int auto_increment primary key,
username varchar(30) not null unique,
INDEX(username)
)ENGINE=INNODB charset=utf8;


create table Server(
id int auto_increment primary key,
ServerName varchar(20) not null unique,
Name varchar(100) not null,
Maplist varchar(20) not null,
Prayers varchar(20) not null,
INDEX(ServerName)
)ENGINE=INNODB charset=utf8;