from http import HTTPStatus

from fastapi import APIRouter, Request
from starlette.templating import _TemplateResponse

from homelab.common import templates


__all__: tuple[str, ...] = (
    "router",
)


router = APIRouter()


@router.get("/")
async def home(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(
        request=request,
        name="home.jinja",
        context={"request": request},
        status_code=HTTPStatus.OK,
    )
