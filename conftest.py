import os
import pytest
import logging


@pytest.fixture(scope="session", autouse=True)
# logging settings
def logger():
    log_dir = "logs"
    log_file = os.path.join(log_dir, "test.log")
    # Create the logs folder if it does not exist.
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(handler)
    return logger