# Start your project here
from tina4_python.Migration import migrate
import os
import logging

from db import dba

# ----- LOGGER -----
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("init_logger")

# ----- ROUTES -----
from .routes import main
from .routes import api

# ----- DATABASE MIGRATIONS -----
run_migrations = os.getenv("RUN_MIGRATIONS_SWITCH")
if run_migrations and run_migrations == "True":
    logger.info("RUNNING MIGRATIONS")
    migrate(dba)
else:
    logger.info("RUN MIGRATIONS IS DEACTIVATED")
