import Mysql_Insert


async def get_img(Query_Login: str) -> str:
    if Query_Login == '色图':
        print(Query_Login)
        c = '[CQ:image,file=file:///E:/2.jpg]'
        return c
    elif Query_Login == '吃瓜':
        return '吃瓜'
    elif Query_Login == '快速链接':
        s = """https://www.ceve-market.org/index/"""
        return s
    elif Query_Login == '劳动仲裁':
        s = "文档：劳动仲裁和劳动法记录.note\n链接：http://note.youdao.com/noteshare?id=13ef9e3ff1cbcd4cb61b459c3e46cabf&sub=8C73DE805D394DF9A6C58AF74D900D06"
        return  s