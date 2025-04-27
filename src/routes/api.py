import logging

from tina4_python.Router import get, post, put, delete
from tina4_python.Swagger import secure

from src.app import user_service

# ----- LOGGER -----
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("api_routes_logger")

@post("/api/user-login")
@secure()
async def post_user_login(request, response):
    data = request.params
    email = data.get("email")
    password = data.get("password")
    login_response = user_service.check_user_credentials(email, password)
    code = round(login_response["code"] / 100) * 100
    return response(login_response, code)
