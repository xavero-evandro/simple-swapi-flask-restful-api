import requests
import json


def getAllStarships(urlApi):
    hasNextPage = True
    page = 1
    starships = []
    while hasNextPage:
        response = requests.get(urlApi+f"/?page={page}")
        if response.status_code != 404:
            starships.extend(response.json()['results'])
            page += 1
        else:
            hasNextPage = False
    return starships


def orderStarships(starships):
    return sorted(
        starships, key=lambda ship: ship['hyperdrive_rating'], reverse=True)


def filterStarshipsResults(starships):
    filteredStarships = {'starships': [],
                         'starships_unknown_hyperdrive': []}
    for i in range(len(starships)):
        if(starships[i]['hyperdrive_rating'] == 'unknown'):
            filteredStarships.get('starships_unknown_hyperdrive').extend([
                {
                    "name": starships[i]['name']
                }
            ])
        else:
            filteredStarships.get('starships').extend([
                {
                    "name": starships[i]['name'],
                    "hyperdrive": starships[i]['hyperdrive_rating']
                }
            ])

    return filteredStarships
