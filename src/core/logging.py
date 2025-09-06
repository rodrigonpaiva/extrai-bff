# src/core/logging.py
import logging
from pythonjsonlogger.json import JsonFormatter


def setup_logging(level: str = "INFO"):
    logger = logging.getLogger()
    log_handler = logging.StreamHandler()
    formatter = JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    log_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(log_handler)
    logger.setLevel(level.upper())

    return logger
