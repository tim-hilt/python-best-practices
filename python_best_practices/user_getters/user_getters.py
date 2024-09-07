import asyncio
import json

import httpx

from python_best_practices.common.types import User, map_dict_to_dataclass


class ShellUserGetter:
    @staticmethod
    async def get_user(id: int) -> User:
        process = await asyncio.create_subprocess_exec(
            "curl",
            f"https://jsonplaceholder.typicode.com/users/{id}",
            stdout=asyncio.subprocess.PIPE,
        )

        stdout, _ = await process.communicate()
        user = map_dict_to_dataclass(json.loads(stdout), User)
        return user


class HttpUserGetter:
    @staticmethod
    async def get_user(id: int) -> User:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"https://jsonplaceholder.typicode.com/users/{id}")
            user = map_dict_to_dataclass(r.json(), User)
            return user


class FileUserGetter:
    @staticmethod
    async def get_user(id: int) -> User:
        with open("assets/users.json", encoding="utf-8") as users_file:
            users = json.load(users_file)
            user = list(filter(lambda u: u["id"] == id, users))[0]  # type: ignore
            return map_dict_to_dataclass(user, User)  # type: ignore
