import asyncio
import json

import httpx

from python_best_practices.common.types import User, map_dict_to_dataclass


class ShellUserGetter:
    @staticmethod
    async def get_user() -> User:
        process = await asyncio.create_subprocess_exec(
            "curl",
            "https://jsonplaceholder.typicode.com/users/1",
            stdout=asyncio.subprocess.PIPE,
        )

        stdout, _ = await process.communicate()
        user = map_dict_to_dataclass(json.loads(stdout), User)
        return user


class HttpUserGetter:
    @staticmethod
    async def get_user() -> User:
        async with httpx.AsyncClient() as client:
            r = await client.get("https://jsonplaceholder.typicode.com/users/1")
            user = map_dict_to_dataclass(r.json(), User)
            return user


class FileUserGetter:
    @staticmethod
    async def get_user() -> User:
        data = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }
        user = map_dict_to_dataclass(data, User)
        return user
