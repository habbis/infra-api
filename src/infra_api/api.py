from roadstead_api.database import get_all_vlan
from roadstead_api.database import get_singel_vlan
from roadstead_api.database import insert_vlan
from roadstead_api.database import update_vlan
from roadstead_api.database import delete_vlan

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

api_route = "v1"


class Vlan(BaseModel):
    name: str
    vlan_id: int
    prefix: str

    model_config = {
        "name": "vlan_name",
        "vlan_id": 333,
        "prefix": "vlan_prefix",
    }

@app.get("/%s/vlan" % api_route)
def get_all_vlan():
    all_vlan = get_all_vlan()
    if all_vlan is None:
        raise HTTPException(status_code=404, detail="Vlan not found")
    else:
        return all_vlan
     # for info in all_vlan:
     #    data = {
     #       "name": info[0],
     #       "vlan_id": info[1],
     #       "prefix": info[2],
     #       "updated": info[3]
     #    }
     #    yield data


@app.get("/%s/vlan/{vlan}" % api_route, response_model=Vlan)
def get_singel_vlan(vlan: str):
    vlan = get_singel_vlan(vlan)
    data = {
        "name": vlan[0],
        "vlan_id": vlan[1],
        "prefix": vlan[2],
        "updated": vlan[3]
    }
    return data


@app.put("/%s/vlan" % api_route)
def create_vlan(vlan: Vlan):
    get_vlan = get_singel_vlan(vlan.name)
    if get_vlan is None:
      add_vlan = insert_vlan(vlan.name, vlan.vlan_id, vlan.prefix)
    else:
      add_vlan = update_vlan(vlan.name, vlan.vlan_id, vlan.prefix, vlan.name)
    return add_vlan
