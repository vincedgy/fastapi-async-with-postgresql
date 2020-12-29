# FastAPI async with Postgresql DB #

> Author : @vincedgy

## Objectives

The main goal of this little demonstration project is to explore [FastAPI](https://fastapi.tiangolo.com/) framework
NOT using [asyncio](https://docs.python.org/3/library/asyncio.html) but a higher level abstraction.

This project is very much inspired by the very framework used tutorial named ['databases'](https://pypi.org/project/databases/)
which gives asyncio support for a range of SQL databases.

The documentation can be find [here](https://www.encode.io/databases/).

## Requirements

The code hase been developed and tested with Python 3.9.1. It is probably ok with Python 3.6+.

- [Python 3.9+](https://python.org)

Package manager :

- [Poetry](https://python-poetry.org/)
  
Used main libraries :

- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [pydantic](https://pydantic-docs.helpmanual.io/)  
- [Databases](https://pypi.org/project/databases/)
- [colorama](https://pypi.org/project/colorama/)

## Installation dependencies

```sh
cd lib
python3 -m poetry install
```

Then activate the shell

```sh
python3 -m poetry shell
```

## Run tests

```sh
cd lib
poetry install
```

