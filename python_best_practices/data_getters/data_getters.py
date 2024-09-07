import asyncio
import json
from typing import Any

import httpx


class ShellDataGetter:
    @staticmethod
    async def get_data() -> dict[str, Any]:
        process = await asyncio.create_subprocess_exec(
            "curl",
            "https://jsonplaceholder.typicode.com/users/1",
            stdout=asyncio.subprocess.PIPE,
        )

        stdout, _ = await process.communicate()
        return json.loads(stdout)


class HttpDataGetter:
    @staticmethod
    async def get_data() -> dict[str, Any]:
        async with httpx.AsyncClient() as client:
            r = await client.get("https://www.example.com/")
            return r.json()


class FileDataGetter:
    @staticmethod
    async def get_data() -> dict[str, Any]:
        await asyncio.sleep(0.05)
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
        return data
