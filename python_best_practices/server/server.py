from typing import Protocol

from litestar import Litestar, get
from litestar.types import ControllerRouterHandler

from python_best_practices.user_getters.user_getters import (
    ShellUserGetter,
    HttpUserGetter,
    FileUserGetter,
)
from python_best_practices.common.types import User


class UserGetter(Protocol):
    @staticmethod
    async def get_user() -> User: ...


async def get_name(getter: UserGetter):
    # Not a good showcase for using Protocols, as the function isn't really doing anything with the data
    return await getter.get_user()


ROUTES: list[ControllerRouterHandler] = []


def register_route(func: ControllerRouterHandler):
    ROUTES.append(func)
    return func


@register_route
@get("/from-shell")
async def from_shell() -> User:
    return await get_name(ShellUserGetter)


@register_route
@get("/from-http")
async def from_http() -> User:
    return await get_name(HttpUserGetter)


@register_route
@get("/from-file")
async def from_file() -> User:
    return await get_name(FileUserGetter)


@register_route
@get("/")
async def index() -> str:
    return "Hello, world!"


router = Litestar(ROUTES)
