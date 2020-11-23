CREATE TABLE `user` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`name` char(20) NOT NULL COMMENT '游戏ID',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`, `name`)
);
CREATE TABLE `weapons` (
`name` char(20) NOT NULL COMMENT '游戏ID',
`weapons_name` char(20) NOT NULL COMMENT '武器名称',
`weapons_kills` char(10) NULL COMMENT '武器击杀数',
`weapons_kpm` char(5) NULL COMMENT '武器每分钟击杀数',
`weapons_accuracy` char(5) NULL COMMENT '武器准度',
`weapons_headshots` char(7) NULL COMMENT '武器爆头数',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`name`, `weapons_name`)
);
CREATE TABLE `recent_sesions` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`name` char(20) NOT NULL COMMENT '游戏ID',
`spm` char(10) NULL COMMENT '每分钟得分数',
`kd` char(10) NULL COMMENT '击杀/死亡比',
`kpm` char(10) NULL COMMENT '每分钟击杀数 ',
`timeplayed` char(15) NULL COMMENT '游戏时间',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`, `name`)
);
CREATE TABLE `vehicles` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`name` char(20) NOT NULL COMMENT '游戏ID',
`vehicles_name` char(20) NOT NULL COMMENT '载具名称',
`vehicles_kills` char(10) NULL COMMENT '载具击杀数',
`vehicles_kpm` char(5) NULL COMMENT '载具每分钟击杀数',
`vehicles_destroyed` char(7) NULL COMMENT '击毁载具数量',
`vehicles_time` char(7) NULL COMMENT '击毁载具数量',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);
CREATE TABLE `new_overview` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`name` char(50) NOT NULL COMMENT '游戏ID',
`rank` char(5) NULL COMMENT '等级',
`win_percent` char(6) NULL COMMENT '胜率',
`kd` char(6) NULL COMMENT 'kd',
`kpm` char(5) NULL COMMENT '每分钟击杀',
`all_kills` char(5) NULL COMMENT '总击杀',
`head_shots_odds` char(5) NULL COMMENT '爆头率',
`accuracy_ratio` char(5) NULL COMMENT '准度',
`infantry_kd` char(5) NULL COMMENT '步兵kd',
`infantry_kpm` char(5) NULL COMMENT '步兵kpm',
`vehicle_kills` char(7) NULL COMMENT '载具击杀',
`vehicle_kpm` char(5) NULL COMMENT '载具每分钟击杀数',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);
CREATE TABLE `server_id` (
`server_id` int(30) NOT NULL COMMENT '服务器ID',
`server_as_name` varchar(10) NOT NULL COMMENT '服务器别名',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`server_id`, `server_as_name`)
);

CREATE TABLE `server` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`server_id` char(15) NOT NULL COMMENT '服务器ID',
`server_name` char(70) NULL COMMENT '服务器名称',
`maplist` char(10) NULL COMMENT '地图',
`mode` char(10) NULL COMMENT '地图',
`prayers` char(6) NULL COMMENT '游戏人数',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);

CREATE TABLE `proposal` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`qq` varchar(20) NOT NULL COMMENT 'qq号',
`idea` varchar(255) NOT NULL COMMENT '建议',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);

CREATE TABLE `relevance` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`qq` varchar(20) NOT NULL COMMENT 'qq号',
`username` varchar(30) NOT NULL COMMENT '建议',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);


CREATE TABLE `statistics` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
`groupid` varchar(20) NOT NULL COMMENT 'qq群',
`module` varchar(20) NOT NULL COMMENT '模块',
`number` varchar(20) NOT NULL COMMENT '数量',
`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
);