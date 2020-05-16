# Swapi Starships Hyperdrive

### Simple api to return all Starship from Star wars sorted by its Hyperdrive Rating

## Docker Approach

### Just run docker-compose to set up everything and run the api:

```
docker-compose up
```

## Normal python 3.+ and pip

### Install dependencies, run:

```
pip install -r requirements.txt
```

### And run:

```
python app.py
```

### The API is going to be running at

```
localhost:5000
```

# Endpoint

## GET /

### Will return a list of all Starships sorted by its Hyperdrive Rating.

#### Response Body Example:

```
{
  "starships": [
    {
      "name": "Belbullab-22 starfighter",
      "hyperdrive": "6"
    },
    {
      "name": "Death Star",
      "hyperdrive": "4.0"
    },
    {
      "name": "Slave 1",
      "hyperdrive": "3.0"
    },
  ],
  "starships_unknown_hyperdrive": [
    {
      "name": "AA-9 Coruscant freighter"
    }
  ]
}
```

# Tests

### To run test just run the api with `python app.py`

```
python app.py
```

### And then run `Pytest`:

```
pytest
```
