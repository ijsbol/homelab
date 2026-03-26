from fastapi.templating import Jinja2Templates


__all__: tuple[str, ...] = (
    "templates",
)


templates = Jinja2Templates(directory="homelab/templates")
