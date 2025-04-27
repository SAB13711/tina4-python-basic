import logging

from tina4_python.Template import Template
from tina4_python.Router import get, post, put, delete
from tina4_python.Swagger import secure

# ----- LOGGER -----
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main_routes_logger")

@get("/user-login")
async def get_user_login(request, response):
    return response(Template.render_twig_template("/forms/pages/login-form-page.twig"))

@get("/landing-page")
async def get_landing_page(request, response):
    return response("This is the landing page!")

@get("/hello/world")
async def get_hello_world(request, response):
    return response("Hello World! Get route")

@post("/hello/world")
@secure()
async def post_hello_world(request, response):
    return response("Hello World! Post route")



