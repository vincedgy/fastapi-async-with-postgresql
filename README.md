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


Obviously you'll need a postgresql database.

We'll be using [locust](https://locust.io) for performance/load testing.



## Installation dependencies

```shell
cd lib
python3 -m poetry install
```

Then activate the shell

```shell
python3 -m poetry shell
```

## Install Postgresql

For this we use docker (choose he appropriate docker desktop for you local OS) with the help of docker-compose.

Please refer to the official documentation of docker and docker-compose for your environment.


Launch the docker-compose stack like so :


```shell
$ docker-compose up -d
Starting fastapi-async-with-postgresql_adminer_1 ... done
Recreating fastapi-async-with-postgresql_db_1    ... done
```

Checkout if the stack is up and running

```shell
$ docker-compose ps
                 Name                                Command               State           Ports
---------------------------------------------------------------------------------------------------------
fastapi-async-with-postgresql_adminer_1   entrypoint.sh docker-php-e ...   Up      0.0.0.0:8080->8080/tcp
fastapi-async-with-postgresql_db_1        docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp
```

From this point you should be able to log on your database with the help of psql also with docker : 

```shell
$ docker run -it --rm --network fastapi-async-with-postgresql_default postgres psql -h db -U vincent -d dev
Password for user vincent:
psql (13.1 (Debian 13.1-1.pgdg100+1))
Type "help" for help.

dev=# \l
                               List of databases
   Name    |  Owner  | Encoding |  Collate   |   Ctype    |  Access privileges
-----------+---------+----------+------------+------------+---------------------
 dev       | vincent | UTF8     | en_US.utf8 | en_US.utf8 |
 postgres  | vincent | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | vincent | UTF8     | en_US.utf8 | en_US.utf8 | =c/vincent         +
           |         |          |            |            | vincent=CTc/vincent
 template1 | vincent | UTF8     | en_US.utf8 | en_US.utf8 | =c/vincent         +
           |         |          |            |            | vincent=CTc/vincent
 vincent   | vincent | UTF8     | en_US.utf8 | en_US.utf8 |
(5 rows)


```

## Run the server

Using poetry runner


```shell
$ cd src
$ poetry run python main.py

Python 2.7 will no longer be supported in the next feature release of Poetry (1.2).
You should consider updating your Python version to a supported one.

Note that you will still be able to manage Python 2.7 projects by using the env command.
See https://python-poetry.org/docs/managing-environments/ for more information.

The currently activated Python version 2.7.16 is not supported by the project (^3.9).
Trying to find and use a compatible version.
Using python3 (3.9.1)
2020-12-29 21:23:39,115:INFO:db_utils:Defining configuration for db at [postgresql://vincent:****@localhost:5432/vincent?sslmode=prefer]
2020-12-29 21:23:39,145:INFO:schema:Defining table 'notes'
2020-12-29 21:23:39,146:INFO:schema:Creating schema
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
2020-12-29 21:23:39,200:INFO:uvicorn.error:Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [47773] using statreload
2020-12-29 21:23:39,200:INFO:uvicorn.error:Started reloader process [47773] using statreload
2020-12-29 21:23:39,458:INFO:db_utils:Defining configuration for db at [postgresql://vincent:****@localhost:5432/vincent?sslmode=prefer]
2020-12-29 21:23:39,484:INFO:schema:Defining table 'notes'
2020-12-29 21:23:39,485:INFO:schema:Creating schema
INFO:     Started server process [47780]
2020-12-29 21:23:39,541:INFO:uvicorn.error:Started server process [47780]
INFO:     Waiting for application startup.
2020-12-29 21:23:39,542:INFO:uvicorn.error:Waiting for application startup.
2020-12-29 21:23:39,559:INFO:databases:Connected to database postgresql://vincent:********@localhost:5432/vincent?sslmode=prefer
INFO:     Application startup complete.
2020-12-29 21:23:39,560:INFO:uvicorn.error:Application startup complete.
```

## Test the server

You can use curl or whatever client for REST API

Create a Note :

```shell
curl -i -X POST http://localhost:5000/notes --data "{\"text\":\"Test\",\"completed\":\"false\"}"
HTTP/1.1 200 OK
date: Tue, 29 Dec 2020 20:25:46 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"text":"Test","completed":false,"id":1}%
```

Request all notes :

```shell
$ curl -i -X GET http://localhost:5000/notes
HTTP/1.1 200 OK
date: Tue, 29 Dec 2020 20:26:36 GMT
server: uvicorn
content-length: 42
content-type: application/json

[{"id":1,"text":"Test","completed":false}]%
```

## Using adminer

`docker-compose.yml` file runs [adminer](https://www.adminer.org), a great php tool for db navigation.

You should open the url http://localhost:8080/?pgsql=db&username=vincent&db=vincent&ns=public&select=notes
and see the content of the "notes" table.

![adminer]

## Run load tests

The project uses [locust](https://locust.io) with a single load test file that you can easily update.

![locust]


```shell
$ cd src
$ poetry run locust -f ../locust/locustfile.py
[2020-12-29 21:55:19,670] yourmachine.local/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2020-12-29 21:55:19,678] yourmachine.local/INFO/locust.main: Starting Locust 1.4.1
[2020-12-29 21:56:09,048] yourmachine.local/INFO/locust.runners: Spawning 10 users at the rate 2 users/s (0 users already running)...
[2020-12-29 21:56:13,564] yourmachine.local/INFO/locust.runners: All users spawned: QuickstartUser: 10 (10 total running)

```

You're invited to open the given http://0.0.0.0:8089

Then you should be able to input a setting 

![locust dialog]


The test begins when you hit the button :

![locust test tab]


You find charts that show the global performance all along tht test

![locust charts]


After a few minutes you should get something like this

![locust charts 2]

---

# Thanks !

[adminer]: resources/adminer.png
[locust]: resources/locust_logo.png
[locust dialog]: resources/locust_dialog.png
[locust test tab]: resources/locust_launch_tab.png
[locust charts]: resources/locust_charts.png
[locust charts 2]: resources/locust_charts_2.png