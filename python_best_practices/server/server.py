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
    async def get_user(id: int) -> User: ...


# TODO: 500 when not found; should really return 404
async def get_name(getter: UserGetter, id: int):
    user = await getter.get_user(id)
    name = user.name
    return name


ROUTES: list[ControllerRouterHandler] = []


def register_route(func: ControllerRouterHandler):
    ROUTES.append(func)
    return func


@register_route
@get("/name/from-shell/{id: int}")
async def from_shell(id: int) -> str:
    return await get_name(ShellUserGetter, id)


@register_route
@get("/name/from-http/{id: int}")
async def from_http(id: int) -> str:
    return await get_name(HttpUserGetter, id)


@register_route
@get("/name/from-file/{id: int}")
async def from_file(id: int) -> str:
    return await get_name(FileUserGetter, id)


@register_route
@get("/")
async def index() -> str:
    return "Hello, world!"


router = Litestar(ROUTES)
