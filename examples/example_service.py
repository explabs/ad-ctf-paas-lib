import requests
from checker import Checker

c = Checker()


@c.ping
def ping():
    r = requests.get(f"http://{c.address}:80")
    if r.status_code == 200:
        return 'pong'


@c.put
def put():
    r = requests.post(f"http://{c.address}/put", json={"flag": c.flag})
    if r.status_code == 200:
        # returns uniq value such as database id
        return r.content


@c.get
def get():
    r = requests.get(f"http://{c.address}/get/{c.uniq_value}")
    if r.status_code == 200:
        # returns flag as string
        return r.content

if __name__ == '__main__':
    c.run()
