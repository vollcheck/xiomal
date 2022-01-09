import requests
import xml.etree.ElementTree as ET

# TODO: 1. get env variable in for API key

# Hard-coded for now
API_KEY = None
value = "Warsaw"


def get_url(value: str) -> str:
    return f"http://api.weatherapi.com/v1/current.xml?key={API_KEY}&q={value}&aqi=no"


def run():
    url = get_url(value)
    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code)
        print("Something went wrong")

    from pprint import pprint

    # pprint(response.text)
    tree = ET.fromstring(response.text)
    pprint(dir(tree))

    for child in tree:
        print(child.tag)


run()
