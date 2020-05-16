import pytest
import requests
from mockStarshipsHyperDriveReturn import mockStarshipsReturn

url = 'http://localhost:5000'  # The root url of the flask app


def test_index_page():
    res = requests.get(url+'/')
    assert res.status_code == 200
    assert res.json() == mockStarshipsReturn()
