import logging
# Create a custom logger
logger = logging.getLogger(__name__)
logging.getLogger("boto3").setLevel("CRITICAL")
logging.getLogger("requests").setLevel("CRITICAL")

# import requests
# requests.get("https://google.com2").text


# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.debug('This is a debug')
logger.info('This is a info')
logger.warning('This is a warning')
logger.error('This is an error')