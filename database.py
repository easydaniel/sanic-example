from asyncpg import create_pool
import config

import sqlalchemy.sql
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.sqltypes import DateTime, NullType, String


class StringLiteral(String):
    """Teach SQLAlchemy how to literalize various things."""

    def literal_processor(self, dialect):
        super_processor = super(StringLiteral, self).literal_processor(dialect)

        def process(value):
            if isinstance(value, int):
                return str(value)
            if not isinstance(value, str):
                value = str(value)
            result = super_processor(value)
            if isinstance(result, bytes):
                result = result.decode(dialect.encoding)
            return result
        return process


class LiteralDialect(postgresql.dialect):
    colspecs = {
        # prevent various encoding explosions
        String: StringLiteral,
        # teach SA about how to literalize a datetime
        DateTime: StringLiteral,
        # don't format py2 long integers to NULL
        NullType: StringLiteral
    }


class DB:

    class base:
        async def execute(self):
            sql = self.compile(dialect=LiteralDialect(), compile_kwargs={
                               "literal_binds": True}, inline=True)
            if not isinstance(self, DB.select):
                # Return result rows instead of psql result
                sql = f'{sql} RETURNING *'
            # Take a connection from the pool.
            async with DB.pool.acquire() as connection:
                # Open a transaction.
                async with connection.transaction():
                    # Run the query passing the request argument.
                    return await connection.fetch(str(sql))

    class select(base, sqlalchemy.sql.selectable.Select):
        pass

    class insert(base, sqlalchemy.sql.dml.Insert):
        pass

    class delete(base, sqlalchemy.sql.dml.Delete):
        pass

    class update(base, sqlalchemy.sql.dml.Update):
        pass


async def init_db():
    DB.pool = await create_pool(**config.DATABASE)
    # Take a connection from the pool.
    async with DB.pool.acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            with open('table.sql', 'r') as sql:
                # Create table
                await connection.execute(sql.read())
