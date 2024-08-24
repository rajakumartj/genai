import logging
import os
from pathlib import Path
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
# os.mkdir(log_path, exist_ok=True)
Path(log_path).mkdir(parents=True, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format='[%(asctime)s] %(lineno)d %(levelname)-8s %(name)-15s %(message)s'

)


