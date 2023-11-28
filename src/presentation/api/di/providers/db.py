from src.ifrastructure.db.uow import UnitOfWork


class DB_provider():
    def __init__(self, pool, db_name):
        self.client=  pool
        self.db_name = db_name
    async def get_session(self):
        async with await self.client.start_session() as session:
            uow = UnitOfWork(session, self.client[self.db_name])
            yield uow

    async def provide_db(self):
        return self.client[self.database_name]
