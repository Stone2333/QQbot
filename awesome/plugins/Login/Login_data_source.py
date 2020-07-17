import Mysql_Insert


async def get_Login(Query_Login: str) -> str:
    for ch in Query_Login:
        if '\u4e00' <= ch <= '\u9fff':
            return 'nmsl输nm中文'
    try:
        Mysql_Insert.Insert_User(Query_Login)
        prompt = "注册成功"
        return prompt
    except:
        prompt = "ID已注册"
        return prompt