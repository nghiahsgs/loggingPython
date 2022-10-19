import logging
name = 'John'


# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)
# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logging.debug(f'This is a debug message22: {name}')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# logging.critical('This is a critical message')


a = 5
b = 0
try:
  c = a / b
except Exception as e:
#   logging.error("Exception occurred")
#   logging.error("Exception occurred", exc_info=True)
    logging.exception("Exception occurred") # log error with exc_info
    

