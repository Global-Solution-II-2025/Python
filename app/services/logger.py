import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name="career_ai"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    handler = RotatingFileHandler("app.log", maxBytes=5_000_000, backupCount=2)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(fmt)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

logger = setup_logger()
