import logging
import os
import pathlib
import uuid

# Setup logging to a local file named using a random uuid4 hash.
root_logger = logging.getLogger()

log_folder = pathlib.Path(f"{pathlib.Path(__file__).parent}/log")

if not log_folder.exists():
    os.mkdir(log_folder)

file_handler = logging.FileHandler(f"{log_folder}/{uuid.uuid4()}.log", encoding="utf-8")
file_handler_formatter = logging.Formatter("[%(asctime)s%(msecs)d][%(levelname)s] %(message)s")
file_handler_formatter.default_msec_format = '%s.%03d'
file_handler.setFormatter(file_handler_formatter)

root_logger.addHandler(file_handler)
