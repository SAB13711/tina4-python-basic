import logging
from db import dba

# ----- LOGGER -----
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("user_service_logger")

def check_user_credentials(email, password) -> dict:
    try:
        user = dba.fetch_one("select * from user where email = ?", [email])
        if not user:
            return {"success": False, "msg": "no user with the given email", "code": 404}
        if not user["password"] == password:
            return {"success": False, "msg": "password does not match email", "code": 400}
        return {"success": True, "msg": "login successful", "code": 200, "user": {
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "email": user["email"],
            "phone": user["phone"]
        }}
    except Exception as e:
        logger.error({"location": "check_user_credentials", "msg": "error while attempting to check user credentials", "error": str(e)})
        return {"success": False, "msg": "error while attempting to check user credentials", "code": 500}
