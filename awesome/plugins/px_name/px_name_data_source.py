import px_select


async def get_px_name_select(Quer_px_name_select):
    px = px_select.Select_company_name(Quer_px_name_select)
    print(px)
    if px == []:
        null = "该公司未在培训库中存在"
        print("该公司未在培训库中存在")
        return null
    else:
        count = 1
        f = ""
        for index in range(len(px)):
            a = ""
            if (index % 2) != 0:
                continue
            c = px[index]
            d = index + 1
            if d < len(px):
                name = px[d]
                if len(name) <= 0:
                    name = "暂无"
            if count > 1:
                a = f + str(count) + ":" + '培训公司名称:' + c + '\n' + '地址:' + name + '\n'
            else:
                a = f + '培训不得house' + '\n' + str(count) + ":" + '培训公司名称:' + c + '\n' + '地址:' + name + '\n'
            f = a
            count = count + 1
        print(f)
        return f





if __name__ =="__main__":
    get_px_name_select("音泰思")
