import asyncio
import httpx
import xml.etree.ElementTree as ET
from data_storage import DataStorage, DataMoex
import os
from dotenv import load_dotenv

DS = DataStorage()
DM = DataMoex()

class Parser:
    async def get_text(self, client, url):
        resp = await client.get(url)
        xml_text = resp.text
        return xml_text


    async def run_parser(self, url):
        async with httpx.AsyncClient() as client:
            tasks = []
            for i in range (1, 20):
                tasks.append(asyncio.create_task(self.get_text(client, url)))
            parsed_text = await asyncio.gather(*tasks)
            DM.add_data(parsed_text)
            # await DS.add_data(parsed_text)


if __name__ == "__main__":
    parser = Parser()
    load_dotenv()
    url=os.getenv('URL')
    asyncio.run(parser.run_parser(url))