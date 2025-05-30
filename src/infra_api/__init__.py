from infra_api.config import env_value
from infra_api.logs import create_logs
#from infra_api import app

debug, _, _, _ = env_value()

def main() -> None:
    create_logs("testing")
