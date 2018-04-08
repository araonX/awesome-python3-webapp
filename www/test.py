#!/home/xiejg/awesome-python3-webapp/env/bin/python3.5
import orm
from models import User, Blog, Comment
import asyncio
async def test(loop, **kw):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'), id=kw.get('id'), admin=kw.get('admin'))
#    u = Blog(id = kw.get('id'), user_id=kw.get('user_id'),user_name=kw.get('user_name'),user_image=kw.get('user_image'),name=kw.get('name'),summary=kw.get('summary'),content=kw.get('content'),created_at=kw.get('created_at')) 
    await u.save()
    await orm.destory_pool()

#data=dict(id='3',user_id='1245',user_name='admin2',user_image='about:blank',name='first article',summary='this is the first article.',content ='tests',created_at=123456.554)
data =dict(id)
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()
