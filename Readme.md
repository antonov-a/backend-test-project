# Installing and running the app

## In Virtualenv
1. Install virtualenv if not installed already
2. Execute `make virtualenv` from root directory to build virtual environment
3. Execute `make run` from root directory to start the application

## As a Docker container
TODO


# Testing

## Pytest

Repository comes with a limited amount of unit tests, which can be run with `make test` from root directory. Please make sure virtualenv is generated according to installation instructions above.

## Postman

Before running postman tests, execute `make seed` with app running to populate the database.
