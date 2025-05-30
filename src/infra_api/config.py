import sys
import os

try:
    from dotenv import load_dotenv
    from dotenv import dotenv_values
except ImportError:
    print("python-dotenv module missing")
    sys.exit(-1)


def env_value():
    load_dotenv()

    debug = os.getenv('ROADSTEAD_API_ENVIRONMENT')
    api_address = os.getenv('ROADSTEAD_API_ADDRESS')
    api_port = os.getenv('ROADSTEAD_API_PORT')
    db_connection = os.getenv('ROADSTEAD_API_DB_CONNECTION')

    return debug, api_address, api_port, db_connection
