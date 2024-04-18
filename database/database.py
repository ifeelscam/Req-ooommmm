import motor.motor_asyncio
from config import Config  #DB_URI, DB_NAME, ADMINS

class Database:
    def __init__(self, uri, database_name):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client[database_name]
        self.users = self.db.users
        self.req_one = self.db.req_one
        self.req_two = self.db.req_two
    
    async def present_user(self, user_id):
        found = await self.users.find_one({'_id': user_id})
        return bool(found)

    async def add_user(self, user_id):
        await self.users.insert_one({'_id': user_id})

    async def full_userbase(self):
        cursor = self.users.find({}, {'_id': 1})
        user_ids = [doc['_id'] async for doc in cursor]
        return user_ids

    async def del_user(self, user_id):
        await self.users.delete_one({'_id': user_id})

    async def is_requested_one(self, message):
        user = await self.get_req_one(message.from_user.id)
        if user:
            return True
        if message.from_user.id in Config.ADMINS:
            return True
        return False
    
    async def is_requested_two(self, message):
        user = await self.get_req_two(message.from_user.id)
        if user:
            return True
        if message.from_user.id in Config.ADMINS:
            return True
        return False

    async def add_req_one(self, user_id):
        try:
            if not await self.get_req_one(user_id):
                await self.req_one.insert_one({"user_id": int(user_id)})
        except:
            pass
        
    async def add_req_two(self, user_id):
        try:
            if not await self.get_req_two(user_id):
                await self.req_two.insert_one({"user_id": int(user_id)})
        except:
            pass

    async def get_req_one(self, user_id):
        return await self.req_one.find_one({"user_id": int(user_id)})

    async def get_req_two(self, user_id):
        return await self.req_two.find_one({"user_id": int(user_id)})

    async def delete_all_one(self):
        await self.req_one.delete_many({})

    async def delete_all_two(self):
        await self.req_two.delete_many({})

db = Database(Config.DATABSE_URL, Config.DATABASE_NAME)
