import asyncio

class DataStorage:
    async def add_data(self, data):
        await asyncio.sleep(1)

class DataMoex(DataStorage):
    def __init__(self):
        self.data_list = []

    async def add_data(self, data):
        self.data_list.append(data)
        await super().add_data(data)

    def get_data(self):
        return self.data_list

