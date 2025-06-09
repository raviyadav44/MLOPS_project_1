from src.logger import logging

# logging.info("This is an info message.")
# logging.debug("This is a debug message.")
# logging.error("This is an error message.")
# logging.warning("This is a warning message.")
# logging.critical("This is a critical message.")

from src.exception import MyException
import sys
# try:
#     # Simulating an error
#     1 / 0
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e