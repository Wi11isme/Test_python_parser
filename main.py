import asyncio
import httpx
import os
from dotenv import load_dotenv
from data_storage import DataMoex

load_dotenv()
url = os.getenv('URL')

DM = DataMoex()

class Parser:
    async def fetch(self, client, url):
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            print(f"An error occurred: {exc}")
            return None

    async def get_text(self, client, url):
        tasks = [asyncio.create_task(self.fetch(client, url)) for _ in range(20)]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        
        for task in pending:
            task.cancel()
        
        for task in done:
            result = task.result()
            if result:
                return result
        return None

    async def run_parser(self, url):
        async with httpx.AsyncClient() as client:
            while True:
                text = await self.get_text(client, url)
                if text:
                    asyncio.create_task(DM.add_data(text))
                await asyncio.sleep(1)

if __name__ == "__main__":
    parser = Parser()
    asyncio.run(parser.run_parser(url))
