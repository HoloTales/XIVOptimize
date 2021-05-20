import requests


class MarketFetch:

    def __init__(self):
        r = requests.get('https://universalis.app/api/marketable/')
        print(r.status_code)
        print(r.headers)
        print(r.text)
        p = r.text
        p = p.replace("[", "")
        arr = p.split(",")
        print(arr)