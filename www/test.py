import orm, asyncio
from models import User


loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome', port=3307)
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop.run_until_complete(test())