import logging
import os

from dotenv import load_dotenv

# gunicorn needs this so leave it
from adapters.api import app


load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=os.getenv("LOG_LEVEL", "INFO"))
