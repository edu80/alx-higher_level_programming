#!/usr/bin/python3
'''Python script that takes a leter and posts'''

if __name__ == "__main__":
    import requests
    import sys

    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    res_json = res.json()
    if res_json == {}:
        print("No result")
    elif res_json.get("id") is None or res_json.get("name") is None:
        print("Not a valid JSON")
    else:
        print(f"[{res_json.get('id')}] {res_json.get('name')}")
