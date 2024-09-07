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
