DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `name` varchar(255) NOT NULL COMMENT '游戏ID',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '游戏用户表';


DROP TABLE IF EXISTS `weapons`;
CREATE TABLE `weapons` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `name` varchar(255) NOT NULL COMMENT '游戏ID',
    `weapons_name` varchar(255) NOT NULL COMMENT '武器名称',
    `weapons_kills` varchar(255) NULL COMMENT '武器击杀数',
    `weapons_kpm` varchar(255) NULL COMMENT '武器每分钟击杀数',
    `weapons_accuracy` varchar(255) NULL COMMENT '武器准度',
    `weapons_headshots` varchar(255) NULL COMMENT '武器爆头数',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '游戏用户表';


DROP TABLE IF EXISTS `recent_sesions`;
CREATE TABLE `recent_sesions` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `name` varchar(255) NOT NULL COMMENT '游戏ID',
    `spm` varchar(255) NULL COMMENT '每分钟得分数',
    `kd` varchar(255) NULL COMMENT '击杀/死亡比',
    `kpm` varchar(255) NULL COMMENT '每分钟击杀数 ',
    `timeplayed` varchar(255) NULL COMMENT '游戏时间',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT 'KDA表';


DROP TABLE IF EXISTS `vehicles`;
CREATE TABLE `vehicles` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `name` varchar(255) NOT NULL COMMENT '游戏ID',
    `vehicles_name` varchar(255) NOT NULL COMMENT '载具名称',
    `vehicles_kills` varchar(255) NULL COMMENT '载具击杀数',
    `vehicles_kpm` varchar(255) NULL COMMENT '载具每分钟击杀数',
    `vehicles_destroyed` varchar(255) NULL COMMENT '击毁载具数量',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '载具表';

DROP TABLE IF EXISTS `overview`;
CREATE TABLE `overview` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `name` varchar(255) NOT NULL COMMENT '游戏ID',
    `score_min` varchar(255) NULL COMMENT '每分钟得分数',
    `kd_ratio` varchar(255) NULL COMMENT '击杀/死亡比',
    `win_percent` varchar(255) NULL COMMENT '胜率',
    `kills_game` varchar(255) NULL COMMENT '场均击杀',
    `kills_min` varchar(255) NULL COMMENT '每分钟击杀数',
    `infantry_kpm` varchar(255) NULL COMMENT '步兵每分钟击杀数',
    `infantry_kd` varchar(255) NULL COMMENT '步兵击杀/死亡比',
    `vehicle_kills` varchar(255) NULL COMMENT '载具击杀数',
    `vehicle_kpm` varchar(255) NULL COMMENT '载具每分钟击杀数',
    `skill` varchar(255) NULL COMMENT '技巧值',
    `accuracy` varchar(255) NULL COMMENT '准度',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '战绩总览表';

DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `server_id` int(15) NOT NULL COMMENT '服务器ID',
    `server_name` varchar(255) NULL COMMENT '服务器名称',
    `maplist` varchar(255) NULL COMMENT '地图',
    `prayers` varchar(255) NULL COMMENT '游戏人数',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '服务器表';







-- 下面是手动创建的培训公司表，其实什么都没有
DROP TABLE IF EXISTS `train_company`;
CREATE TABLE `train_company` (
    `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `company_name` varchar(255) NOT NULL COMMENT '培训名称',
    `company_address` varchar(255) NULL COMMENT '培训地址',
    `create_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
    `update_time` timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '服务器表';
