import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_dir = ".\\Logs"
        log_file = os.path.join(log_dir, "automation.log")

        # Ensure Logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger()

        # Clear existing handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO,
                            force=True)
        return logger