import xml.etree.ElementTree as ET
from typing import List

import click
import requests

from load_env import VARIABLES as V

API_KEY = V.get("API_KEY")


@click.command()
@click.argument("city", type=str)
def request(city: str) -> ET.Element:
    tree = perform_request(city)
    if not tree:
        return
    parsed_tree = parse_tree(tree)
    raport(city, parsed_tree)


def perform_request(city):
    url = f"http://api.weatherapi.com/v1/current.xml?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"There is no city called {city}")
        return

    return ET.fromstring(response.text)


def xget(element: ET.Element, path: List[str]) -> str:
    for step in path:
        element = element.find(step)

    return element.text


def parse_tree(tree: ET.Element) -> dict:
    relevant = {
        "Country": ["location", "country"],
        "Local time": ["location", "localtime"],
        "Air condition": ["current", "condition", "text"],
        "Pressure": ["current", "pressure_mb"],
        "Temperature (°C)": ["current", "temp_c"],
        "Feels like temperature (°C)": ["current", "feelslike_c"],
    }

    data = {k: xget(tree, v) for k, v in relevant.items()}
    data['Teperature (F)'] = (float(data['Temperature (°C)']) * 9/5) + 32
    return data


def raport(city: str, parsed_tree: dict) -> None:
    print(f"You've requested data for '{city}'")

    for k, v in parsed_tree.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    request()
