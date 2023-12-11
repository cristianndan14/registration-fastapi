from dotenv import load_dotenv

from config.util import Environment
from logger import logger

"""load environment variables"""

# Load env variables from a file, if exists else default would be set
logger.info("SERVER_INIT::Setting environment variables from .env file(if exists)...")
load_dotenv(verbose=True)


class DB:
    host = Environment.get_string("DB_HOST", "mysql_db")
    port = Environment.get_string("DB_PORT", "3306")
    name = Environment.get_string("DB_NAME", "devdb")
    user = Environment.get_string("DB_USER", "root")
    pass_ = Environment.get_string("DB_PASS", "admin1234")
