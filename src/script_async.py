import aiohttp
import asyncio
from functools import reduce


API1 = 'endpoint_1'
API2 = 'endpoint_2'
API3 = 'endpoint_3'
DATA_SOURCES = [API1, API2, API3]


class DataHelper:

    BASE_URL = 'http://localhost:8000/'

    def __init__(self, data_sources):
        self._data_sources = data_sources

    @staticmethod
    async def fetch(session, url):
        async with session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            return await response.json()

    async def get_member_data(self, member_id: int):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for endpoint in self._data_sources:
                url = f'{self.BASE_URL}{endpoint}?member_id={member_id}'
                task = asyncio.create_task(DataHelper.fetch(session, url))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
        return results


def data_consolidator(responses: list):
    all_keys = reduce((lambda x, y: x | y), [d.keys() for d in responses])
    max_dict = {k: max(d.get(k, 0) for d in responses) for k in all_keys}
    return max_dict


async def main():
    data_helper = DataHelper(DATA_SOURCES)
    responses = await data_helper.get_member_data(1234)
    print(data_consolidator(responses))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
