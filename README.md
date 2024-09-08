# Python Best Practices

## Setup

- Install [Poetry](https://python-poetry.org/docs/#installation)
- Open project in VS Code
- Install recommended extensions
- Run `http://localhost:8000/schema)poetry install` in the root directory of the project

## Running the Project

``` bash
poetry run python -m python_best_practices
```

## Running the Unit Tests

``` bash
poetry run python -m unittest discover -p "*_test.py"
```

## OpenAPI Schema

Litestar generates an OpenAPI schema for the current app. Navigate to `http://localhost:8000/schema` to take a look at the OpenAPI UI.

## Calculate Code Coverage

Run the following commands to take an in depth look at the projects test-coverage:

``` bash
poetry run coverage run --branch --omit="*_test.py,__init__.py" -m unittest discover -p "*_test.py"
poetry run coverage html
cd htmlcov
python -m http.server
```

Now open up http://localhost:8000 in a web browser to see the results.
