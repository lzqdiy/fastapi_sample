import logging

from app.db.init_db import init_db
from app.db.session import db_session

import os
os.sys.path.append(r"E:\FastAPI_NO.38\all\backend\app")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init():
    init_db(db_session)


def main():
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
