import logging
import sys

from pythonjsonloger.json import jsonFormatter

logger = logging.getLogger("extrai-bff")

logHandler = logging.StreamHandler()
formatter = jsonFormatter(
    defaults={
      "app_name": "extrai-bff",
      "environment": "development",
      },
    fmt="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.info("Logger initialized",
  extra={
    "environment": "development",
  }
    
)