import logging, sys
from python_json_logger import jsonlogger

def setup_logging(level: str = "INFO"):
    handler = logging.StreamHandler(sys.stdout)
    fmt = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(fmt)
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level.upper())