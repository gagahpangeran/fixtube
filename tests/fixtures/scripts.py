import os
import json
import requests


def get_json_data(filename: str, url: str):
    file_path = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(file_path):
        r = requests.get(url)
        with open(file_path, "w") as f:
            f.write(r.text)

    with open(file_path, "r") as f:
        return json.loads(f.read())


def get_fixture_video_info():
    filename = "info.json"
    url = "https://gist.githubusercontent.com/gagahpangeran/500af5bda186454b9f3f326671069e4b/raw/10177a92e4681ccf2656487efefc640053485de0/info.json"
    return get_json_data(filename, url)
