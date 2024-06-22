# __init__.py (root)
# from . import models
import threading
import uvicorn
from . import models
from . import controllers

# models/__init__.py
# from . import res_users

# controllers/__init__.py
# from odoo.addons import fastapi
# from controllers import fastapi_server
# from controllers import fastapi_controller

# Import and run the install script
# from . import install_dependencies
# install_dependencies.install_requirements()


def start_fastapi():
    uvicorn.run(controllers.fastapi_server.app, host="127.0.0.1", port=8000)

def start_fastapi_in_thread():
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()

# Call the function to start FastAPI when your module is initialized
start_fastapi_in_thread()