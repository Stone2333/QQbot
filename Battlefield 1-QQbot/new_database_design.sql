CREATE TABLE `user` (
`id` int(255) NOT NULL AUTO_INCREMENT,
`name` char(30) NOT NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`, `name`) 
);
CREATE TABLE `weapons` (
`name` varchar(50) NOT NULL,
`weapons_name` varchar(30) NOT NULL,
`weapons_kills` varchar(30) NULL,
`weapons_kpm` varchar(30) NULL,
`weapons_accuracy` varchar(30) NULL,
`weapons_headshots` varchar(30) NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`name`, `weapons_name`) 
);
CREATE TABLE `recent_sesions` (
`id` int(255) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`spm` varchar(30) NULL,
`kd` varchar(30) NULL,
`kpm` varchar(30) NULL,
`timeplayed` varchar(30) NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`, `name`) 
);
CREATE TABLE `vehicles` (
`name` varchar(50) NOT NULL,
`vehicles_name` varchar(50) NOT NULL,
`vehicles_kills` varchar(30) NULL,
`vehicles_kpm` varchar(30) NULL,
`vehicles_destroyed` varchar(30) NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`name`, `vehicles_name`) 
);
CREATE TABLE `overview` (
`name` varchar(50) NOT NULL,
`score_min` varchar(30) NULL,
`kd_ratio` varchar(30) NULL,
`win_percent` varchar(30) NULL,
`kills_game` varchar(30) NULL,
`kills_min` varchar(30) NULL,
`infantry_kpm` varchar(30) NULL,
`infantry_kd` varchar(30) NULL,
`vehicle_kills` varchar(30) NULL,
`vehicle_kpm` varchar(30) NULL,
`skill` varchar(30) NULL,
`accuracy` varchar(30) NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`name`) 
);
CREATE TABLE `server_id` (
`server_id` int(30) NOT NULL,
`server_as_name` varchar(100) NOT NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`server_id`, `server_as_name`) 
);
CREATE TABLE `server` (
`server_id` int(30) NOT NULL,
`server_name` varchar(50) NULL,
`maplist` varchar(30) NULL,
`prayers` varchar(30) NULL,
`update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`server_id`) 
);
