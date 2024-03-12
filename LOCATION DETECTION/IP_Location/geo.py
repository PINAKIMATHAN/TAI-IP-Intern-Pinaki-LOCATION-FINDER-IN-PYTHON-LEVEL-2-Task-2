import requests
import json

BASE_URL = "https://get.geojs.io/v1/ip"
session = requests.Session()  # Creates a session to reuse connection


def fetch_data(endpoint):
    try:
        response = session.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()  # Raises an exception for HTTP errors
        
        if response.headers['Content-Type'] == 'application/json':
            return response.json()
        else:
            return response.text.strip()

    except requests.HTTPError as http_err:
        if response.status_code == 404:
            return "Data not available"
        else:
            return f"HTTP error occurred: {http_err}"
    except requests.RequestException as req_err:
        return f"Error fetching data: {req_err}"


def getIP():
    return fetch_data('')


def getCountry(ipAddress, returnType='plain'):
    endpoints = {
        'plain': f"/country/{ipAddress}",
        'plainfull': f"/country/full/{ipAddress}",
        'json': f"/country/{ipAddress}.json"
    }
    return fetch_data(endpoints.get(returnType, ''))


def getGeoData(ipAddress):
    return fetch_data(f"/geo/{ipAddress}.json")


def getPTR(ipAddress):
    return fetch_data(f"/dns/ptr/{ipAddress}")


def showIpDetails(ip=''):
    if not ip:
        ip = getIP()
    geoData = getGeoData(ip)
    print("\nIP Details for:", ip)
    print("-" * 40)
    for key, value in geoData.items():
        print(f"{key.capitalize():<20}: {value}")
    print("-" * 40)


def showCountryDetails(ip=''):
    if not ip:
        ip = getIP()
    countryData = getCountry(ip, 'json')
    print("\nCountry Details for:", ip)
    print("-" * 40)
    for key, value in countryData.items():
        print(f"{key.capitalize():<20}: {value}")
    print("-" * 40)
