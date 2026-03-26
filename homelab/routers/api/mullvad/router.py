from aiohttp import ClientSession
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter(
    prefix="/api/mullvad",
)


class APIMullvadHealthResponse(BaseModel):
    connected: bool
    city: str


@router.get("/health")
async def api_mullvad_health() -> APIMullvadHealthResponse:
    async with ClientSession() as session:
        async with session.get("https://am.i.mullvad.net/json") as response:
            json_response = await response.json()

    return APIMullvadHealthResponse(
        connected=json_response["mullvad_exit_ip"],
        city=json_response["city"].upper(),
    )
