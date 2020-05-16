PYTHON BACKEND

Create a Flask project that exposes a REST API endpoint. When called via the GET method, this endpoint should retrieve a list of all starships from the Star Wars movies (provided by SWAPI), sorted by the hyperdrive rating.

Data source:

Collect the starships from SWAPI. The parameter from the SWAPI used to define the hyperdrive rating of a starship is “hyperdrive_rating”.

https://swapi.co/api/starships/

Response:

A JSON object with the following structure

· starships = A list of starships that have hyperdrive rating. Sorted by hyperdrive rating in ascending order. The elements in the list should contain the name and the hyperdrive rating of the starship.

· starships_unknown_hyperdrive = A list of starships that the hyperdrive rating is unknown. The elements in the list should contain the name of the starship.

Example:

{

"starships":[

{"name": "starship 4", "hyperdrive" : 0.1},

{"name": "starship 1", "hyperdrive" : 0.3},

{"name": "starship 6", "hyperdrive" : 0.5},

{"name": "starship 2", "hyperdrive" : 3.0},

{"name": "starship 5", "hyperdrive" : 4.9}

],

"starships_unknown_hyperdrive": [

{"name": "starship 8"},

{"name": "starship 3"}

]

}

Deliverable:

- Source code

- Deployment instructions

- In case you had any doubt regarding the requirements and made an assumption, just describe what was the doubt and your thinking process.

How to deliver:

Publish your code in a repository of your choice or send a compressed file via email (job@altagram.com).

Curiosity / Reference:

What is hyperdrive?

https://starwars.fandom.com/wiki/Hyperdrive
