import argparse
import xml.etree.ElementTree as ET

import requests

from load_env import VARIABLES as V

# TODO: 1. get env variable in for API key

# Hard-coded for now
API_KEY = V.get("API_KEY")


def run(city: str):
    url = f"http://api.weatherapi.com/v1/current.xml?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code)
        print("Something went wrong")

    tree = ET.fromstring(response.text)

    for child in tree:
        print(child.tag)


# todo: fix parser
# todo: update readme

parser = argparse.ArgumentParser(description='Receive weather information about given city.')

parser.add_argument('city', type=str,
                    help='City to request weather information about.')

args = parser.parse_args()
print(args.accumulate(args.integers))


city = "Warsaw"
run(city)
