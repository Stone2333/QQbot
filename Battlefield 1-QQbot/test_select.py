import Mysql_Select


all_name = Mysql_Select.Select_All_User()

name = Mysql_Select.Select_User("BF_StoneGOGOGO")

server = Mysql_Select.Select_Server("ZBW")

overview = Mysql_Select.Select_Overview("BF_StoneGOGOGO")

weapons = Mysql_Select.Select_Weapons("BF_StoneGOGOGO")

vehicles = Mysql_Select.Select_Vehicles("BF_StoneGOGOGO")

recent_sessions = Mysql_Select.Select_Recent_Sessions("BF_StoneGOGOGO")
