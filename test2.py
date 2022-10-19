from logging import getLogger,StreamHandler,DEBUG


logger = getLogger(__name__)

# c_handler = StreamHandler()
# c_handler.setLevel(DEBUG)
# logger.addHandler(c_handler)

logger.debug("zz")
logger.warning('This is a warning')
logger.error('This is an error')