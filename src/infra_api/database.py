import psycopg

from infra_api.config import env_value

env_db_connection = env_value()
db_connection = env_db_connection[3]

def db_connect():
    dbcon = psycopg.connect(conninfo=db_connection)
    return dbcon


def select_all_vlan():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT name,vlan_id,prefix,updated FROM vlan")
    data = cur.fetchall()
    cur.close()
    conn.close()
    if data is None:
      return None
    else:
      return data

def select_singel_vlan(name):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT name,vlan_id,prefix,updated FROM vlan where name=%s", (name,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data is None:
        return None
    else:
        return data

def insert_vlan(name: str, vlan_id: int, prefix: str):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO vlan (name, vlan_id, prefix) VALUES (%s, %s, %s)", (name, vlan_id, prefix))
    conn.commit()
    cur.close()
    conn.close()

def update_vlan(name: str, vlan_id: int, prefix: str, vlan_name: str):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("UPDATE vlan SET name = %s, vlan_id = %s, prefix = %s WHERE name=%s", (name, vlan_id, prefix, vlan_name))
    conn.commit()
    cur.close()
    conn.close()

def delete_vlan(name: str):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM vlan WHERE name=%s", (name))
    conn.commit()
    cur.close()
    conn.close()
