import json
from requests_oauthlib import OAuth2Session


def connect_wunderlist(filename):
    with open(filename) as f:
        secret_keys = json.load(f)
    
    wunderlist = OAuth2Session()
    wunderlist.headers['X-Client-ID'] = secret_keys["client_id"]
    wunderlist.headers['X-Access-Token'] = secret_keys["access_token"]
    
    return wunderlist

def post_list(wunderlist, title, due_date, list_id):
    url = "https://a.wunderlist.com/api/v1/tasks"
    params = {
        "list_id": list_id,
        "title":title,
        "due_date":due_date
    }
    req = wunderlist.post(url, json=params)

    if req.status_code == 201:
        pass
    else:
        print("Error:{}".format(req.status_code))


def show_tasks_id(wunderlist, list_id):
    url = "https://a.wunderlist.com/api/v1/tasks"
    params = {
        "list_id": list_id,
    }

    req = wunderlist.get(url, params=params)

    tasks = json.loads(req.text)

    id_list = []
    for i in tasks:
        id_list.append(i["id"])

    return id_list


def delete_tasks(wunderlist, task_id):
    url = "https://a.wunderlist.com/api/v1/tasks/" + str(task_id)
    params = {
        "revision": 1,
    }

    req = wunderlist.delete(url, params=params)

 
