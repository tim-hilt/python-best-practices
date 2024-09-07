import asyncio

import uvicorn

from .server import router


async def main():
    config = uvicorn.Config(router, port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


asyncio.run(main())
