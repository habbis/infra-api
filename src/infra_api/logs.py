import logging
from roadstead_api.config import env_value

evn_debug = env_value()
debug = evn_debug[0]


def create_logs(*command):
    if debug == "development":
        logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(message)s', encoding='utf-8',
                            datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
        logging.debug(f"{command}")
    if debug == "production":
        logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(message)s', encoding='utf-8',
                            datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
        logging.info(f"{command}")
