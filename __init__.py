from . import models
from .controllers import fastapi_server

fastapi_server.start_fastapi_in_thread()