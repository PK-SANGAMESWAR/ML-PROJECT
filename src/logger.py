import logging
import os
from datetime import datetime



# 1. Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# 2. Define the directory where logs will be stored
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# 3. Create the logs directory if it doesn't exist
os.makedirs(logs_path,exist_ok=True)

# 4. Construct the full path to the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)



# 5. Configure the basic logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")