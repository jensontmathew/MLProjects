# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)d - %(levelname)s %(message)s",
#     level=logging.INFO
# )

# if __name__ == "__main__":
#     logging.info("Logging has started.")


import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    print(f"Logging to: {LOG_FILE_PATH}")