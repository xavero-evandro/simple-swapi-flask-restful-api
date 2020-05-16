from swapi_integration import getAllStarships, orderStarships, filterStarshipsResults
from mockOrderedStarships import mockOrderedStarships
from mockFilteredStarships import mockFilteredStarships
import json


def test_orderStartShip():
    with open('starships_mock.json') as json_file:
        starshipsMock = json.load(json_file)
    ordenedStarships = orderStarships(starshipsMock['results'])
    assert ordenedStarships == mockOrderedStarships()


def test_filterStarshipsResults():
    filteredStarships = filterStarshipsResults(mockOrderedStarships())
    print(filteredStarships)
    assert filteredStarships == mockFilteredStarships()
