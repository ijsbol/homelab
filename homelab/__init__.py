from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from homelab.routers import router as home_router
from homelab.routers.api.mullvad.router import router as mullvad_router


__all__: tuple[str, ...] = ()


@asynccontextmanager
async def lifecycle(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifecycle,
)

app.mount(
    path="/static",
    app=StaticFiles(directory="homelab/static"),
    name="static",
)

app.include_router(home_router)
app.include_router(mullvad_router)
