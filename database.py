from app import app

async def execute(sql):
    async with app.pool.acquire() as con:
        return await con.execute(sql)
