import configparser
import os
import pathlib
import datetime
import logging


# Create and configure logger
current_day = datetime.datetime.now().strftime("%Y%m%d")

logging.basicConfig(filename=f"logs\{current_day}_log.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

logger.info("####################")
logger.info("Script started")

# read config.ini file
logger.info("Reading config")
config = configparser.ConfigParser()
config.read('config\config.ini')
config_default = config['DEFAULT']

def main():

    logger.info(f"Checking directory {config_default['directoryPath']}")

    for one_file in os.listdir(config_default['directoryPath']):
        logger.info(f"Checking file {one_file}")
        absolute_file_path = os.path.join(config_default['directoryPath'], one_file)
        creation_time = os.path.getctime(absolute_file_path)
        creation_time = pathlib.Path(absolute_file_path).stat().st_ctime
        creation_time = datetime.datetime.fromtimestamp(creation_time)

        time_change = datetime.timedelta(days=7)
        
        if creation_time + time_change < datetime.datetime.now():
            logger.info(f"Deleting file {absolute_file_path}")
            os.remove(absolute_file_path)

if __name__ == "__main__":
    main()

logger.info("Script ended")
logger.info("####################")
