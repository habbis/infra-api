from flask import Flask, jsonify, request, make_response

from infra_api import create_logs
from infra_api.database import insert_vlan
from infra_api.database import update_vlan
from infra_api.database import delete_vlan
from infra_api.database import select_all_vlan
from infra_api.database import select_singel_vlan
from infra_api.config import env_value
import psycopg


env_db_connection = env_value()
db_connection = env_db_connection[3]


def db_connect():
    dbcon = psycopg.connect(conninfo=db_connection)
    return dbcon


debug, _, _, _ = env_value()

app = Flask(__name__)

api_route = "v1"

@app.get("/%s/vlan" % api_route)
def get_all_vlan():
    all_vlan = select_all_vlan()
    data2 = []
    for info in all_vlan:
         data2.append({"name":info[0], "vlan_id": info[1], "prefix":info[2], "update": info[3]})

    #data3 = dict(enumerate(data2))
    return jsonify(data2)

@app.post("/%s/vlan" % api_route)
def post_create_vlan():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' and request.method == 'POST':
        data = request.get_json()
        add_vlan = insert_vlan(data['name'], data['vlan_id'], data['prefix'])
        return add_vlan
    return jsonify()

@app.put("/%s/vlan" % api_route)
def put_create_vlan():
    data = request.get_json()
    get_vlan = select_singel_vlan(data['name'])
    content_type = request.headers.get('Content-Type')
    if get_vlan is None and content_type == 'application/json' and request.method == 'PUT':
        add_vlan = insert_vlan(data['name'], data['vlan_id'], data['prefix'])
        create_logs(add_vlan)
    elif get_vlan is not None and content_type == 'application/json' and request.method == 'PUT':
        add_vlan = update_vlan(data['name'], data['vlan_id'], data['prefix'],data['name'])
        create_logs(add_vlan)
    return jsonify({'messsage':'Success','status_code':200})


@app.get("/%s/vlan/<string:vlan>" % api_route)
def get_singel_vlan(vlan):
    vlan = select_singel_vlan(vlan)
    data = {
        "name": vlan[0],
        "vlan_id": vlan[1],
        "prefix": vlan[2],
        "updated": vlan[3]
    }
    return jsonify(data)


if __name__ == '__main__':
    if debug == "development":
       app.run(debug=True)
    else:
       app.run(host='0.0.0.0')