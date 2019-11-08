import Mysql_Insert
import Mysql_Update

async def get_Login(Query_Login: str) -> str:
    try:
        Mysql_Insert.Insert_User(Query_Login)
        prompt = "注册成功"
        return prompt
    except:
        prompt = "ID已注册"
        return prompt