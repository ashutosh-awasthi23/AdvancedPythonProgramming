import logging

# logging.basicConfig(filename='basicConfig.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')

# advanced configuration
logger = logging.getLogger('advancedConfig_logger')
handler = logging.FileHandler('advancedConfig.log')
formatter = logging.Formatter('%(asctime)s- %(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug("Aaryan")
logger.info("Info message")
