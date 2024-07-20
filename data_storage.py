import asyncio


class DataStorage:
    data = ""

    def __init__(self):
        pass

    async def add_data(self, data):
        await asyncio.sleep(1)

class DataMoex(DataStorage):
    data = ""
    async def add_data(self, data):
        self.data = data
        return await super().add_data(data)