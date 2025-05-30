from roadstead_api.config import env_value
from roadstead_api.logs import create_logs

debug, api_address, api_port, db_connection = env_value()

def main() -> None:
    create_logs("testing")
    print(debug)
    print(api_address)
    print(api_port)
    print(db_connection)
    print("Hello from roadstead-api!")
