# src/main.py

import os
import pandas as pd
import requests
import usaddress

key = os.getenv('GOOGLE_MAPS_KEY')
radius = 500000
systems = [
    {
        'name': 'Medstar',
        'location': '38.9292289,-77.0170727'
    }
]
excelFile = os.path.join(os.getcwd(), 'out', 'results.xlsx')

def query(systemName: str, systemLocation: str, radius: int, key: str):
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={systemName.replace(" ", "+")}+Urgent+Care&location={systemLocation}&radius={radius}&type=health&key={key}'
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        data = response.json()
        dateResults = data['results']
        for dateResult in dateResults:
            name = dateResult['name']
            address = dateResult['formatted_address']
            location, _ = usaddress.tag(address)
            postal = location.get('ZipCode')
            results.append({
                'system': systemName,
                'name': name,
                'postal': postal
            })
        
        if 'next_page_token' in data:
            nextPageToken = data['next_page_token']
            nextPageResults = query(systemName, systemLocation, radius, nextPageToken)
            results.extend(nextPageResults)
    else:
        print(f'Failed to fetch data for .')
        print(f'Status code: {response.status_code}')
    return results

def main():
    results = []
    for system in systems:
        systemName = system['name']
        systemLocation = system['location']
        print(f"Searching for '{systemName}'...")
        systemResults = query(systemName=systemName, systemLocation=systemLocation, radius=radius, key=key)
        results.extend(systemResults)
        print(f"Retrieved results for '{systemName}'.")
    
    data = pd.json_normalize(results)
    data.to_excel(excelFile, index=False)

if __name__ == "__main__":
    main()
