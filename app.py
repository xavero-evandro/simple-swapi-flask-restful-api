from flask import Flask
from flask_restful import Resource, Api
from swapi_integration import getAllStarships, orderStarships, filterStarshipsResults

app = Flask(__name__)
api = Api(app)


class Starships(Resource):
    def get(self):
        starships = getAllStarships("https://swapi.dev/api/starships")
        orderedStarships = orderStarships(starships)
        filteredResults = filterStarshipsResults(orderedStarships)
        return filteredResults


api.add_resource(Starships, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
