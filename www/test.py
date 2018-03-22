#!/home/xiejg/awesome-python3-webapp/env/bin/python3.5
import orm
from models import User, Blog, Comment
import asyncio
async def test(loop, **kw):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'), id=kw.get('id'))
    await u.save()
    await orm.destory_pool()

data=dict(name='xjg', email='1011000@qq.com', passwd='13241', image='about:blank', id='1245')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()
