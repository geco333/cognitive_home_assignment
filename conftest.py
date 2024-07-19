import logging
import uuid

# Setup logging to a local file named using a random uuid4 hash.
logging.basicConfig(force=True)

root_logger = logging.getLogger()

file_handler = logging.FileHandler(f"{uuid.uuid4()}.log", encoding="utf-8")
file_handler_formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
file_handler.setFormatter(file_handler_formatter)

root_logger.addHandler(file_handler)
