from typing import Protocol, Any

from litestar import Litestar, get
from litestar.types import ControllerRouterHandler

from python_best_practices.data_getters.data_getters import (
    ShellDataGetter,
    HttpDataGetter,
    FileDataGetter,
)


class DataGetter(Protocol):
    @staticmethod
    async def get_data() -> dict[str, Any]: ...


async def get_data(getter: DataGetter):
    return await getter.get_data()


ROUTES: list[ControllerRouterHandler] = []


def register_route(func: ControllerRouterHandler):
    ROUTES.append(func)
    return func


@register_route
@get("/from-shell")
async def from_shell() -> dict[str, Any]:
    return await get_data(ShellDataGetter)


@register_route
@get("/from-http")
async def from_http() -> dict[str, Any]:
    return await get_data(HttpDataGetter)


@register_route
@get("/from-file")
async def from_file() -> dict[str, Any]:
    return await get_data(FileDataGetter)


@register_route
@get("/")
async def index() -> str:
    return "Hello, world!"


router = Litestar(ROUTES)
