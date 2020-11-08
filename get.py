import aiohttp
async def fetch(session, url):
    async with session.get(url) as r:
        return await r.text()


async def get_session(url):
    word = []
    async with aiohttp.ClientSession() as s:
        for i in range(1):
            ret = await fetch(s, url)
            word.append(ret)
        return ret

def main(url):
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_session(url)) for i in
             range(1)]
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        task.result()
    return task.result()