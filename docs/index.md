# FastAPI, asyncio with Postgresql #

> Author : @vincedgy

!!! Note

    This documentation uses the excellent `mkdocs` technical documentation static website generator that you can find
    at [mkdocs.org](https://www.mkdocs.org). See more [here](#mkdocs)

You'll find the repository
at [https://github.com/vincedgy/fastapi-async-with-postgresql](https://github.com/vincedgy/fastapi-async-with-postgresql)

Let's do this :rocket:



---

## Objectives

The main goal of this little demonstration project is to explore [FastAPI](https://fastapi.tiangolo.com/) :octicons-heart-fill-24:{: .heart } framework
using [asyncio](https://docs.python.org/3/library/asyncio.html) WITH a higher level abstraction
named [databases](https://pypi.org/project/databases/) connected to a SQL (not async io by nature) PostgreSQL database.

This project is very much inspired by the tutorial of the ***databases*** framework itself that you can find
at ['databases' QuickStart](https://www.encode.io/databases/#quickstart)
which gives asyncio support for a range of SQL databases.

Enjoy 🍺 !

!!! Note

    If you are installing Python on Windows, be sure to check the box to have
    Python added to your PATH if the installer offers such an option (it's
    normally off by default).

## Things I consider...

I should do in the future :

- [ ] : Make a proper Docker file and puch it to the Cloud
- [ ] : Have a look at [asyncpg](https://github.com/magicstack/asyncpg)
- [ ] : Make this project work on [cockroach](https://www.cockroachlabs.com/db/cockroachdb) database instead of
  Postgresql
- [ ] : Add a light [Flask](https://flask.palletsprojects.com/en/1.1.x/) FrontEnd with [svelte](https://svelte.dev)
  FrontEnd, for REST API interactions
- [ ] : Checkout the excellent [https://github.com/vinta/awesome-python](https://github.com/vinta/awesome-python) for
  more inspiration.

:smile:

---

## Requirements

The code hase been developed and tested with Python 3.9.1. It is probably ok with Python 3.6+.

- [Python 3.9+](https://python.org)

### Package manager

This project use the marvelous [Poetry](https://python-poetry.org/) package manager and builder.

It handles dependencies management, locking version and publishing to pypi automagically.

It eases your day to day Python development projects with a lot a easy command to install a virtual environment and
manage dependencies in a very secured way.

### Project's main libraries

This project put together a lot a of great Python libs :

- [FastAPI](https://fastapi.tiangolo.com/) : the blasting fast REST API framework
- [uvicorn](https://www.uvicorn.org/) : the bullet speed ASGI server of reference
- [pydantic](https://pydantic-docs.helpmanual.io/) : the great shema manager
- [Databases](https://pypi.org/project/databases/) : the defacto asyncio lib for many SQL Databases
- [colorama](https://pypi.org/project/colorama/) : the best color'ish lib ever

### Other needs...

Obviously you'll need a postgresql database, but we will have some help with docker if you don't have postgresql 9+
installed locally on your machine.

### But also...

We'll be using the incredible easy to use  [locust](https://locust.io) for performance/load testing.


--- 

## Automation with Makefile

A `Makefile` automates all the commands you need for you.

You'll find description of every command by typing `make help`.

```shell
$ make help
Wed Dec 30 23:35:52 CET 2020
#                                   
#   __  __     ______     __         ______    
#  /\ \_\ \   /\  ___\   /\ \       /\  == \   
#  \ \  __ \  \ \  __\   \ \ \____  \ \  _-/   
#   \ \_\ \_\  \ \_____\  \ \_____\  \ \_\     
#    \/_/\/_/   \/_____/   \/_____/   \/_/     
#                                                 
# ---------------HELP------------------------------------
# - Setup the project              : make install
# - Run the server (blocking)      : make start
# - Evaluate status of the server  : make status
# - Stop (kill) the server         : make kill
# - Tail the current log file      : make tail
# - Run tests on a running server  : make tests
# - Run tests on a running server  : make load_tests
# - Launch mkdocs server Run       : make serve
# - Publish docs GitHub pages      : make publish
# --------------------------------------------------------
Enjoy 🍺 !

```

---

## Install dependencies

Using poetry it's like :

```shell
python3 -m poetry install
```

You can also use `Makefile` commands, like :

```shell
make install
```

Then, you should activate the shell

```shell
python3 -m poetry shell
```

From this point you can use the IDE of your choice.

----

## Run Postgresql with Docker

If you don't have any local [postgresql](https://www.postgresql.org) instance on your local machine, you can use the
provided `docker-compose` stack.

Of course, you'll need to choose the appropriate `docker` installation (you should install the proper `docker desktop`
for your local OS) and install the `docker-compose` utility tool as well

!!! Note

    Please refer to the official documentations of `docker` and `docker-compose` for your environment.

### Launch docker-compose

Launch the docker-compose stack like so :

```shell
$ docker-compose up -d
Starting fastapi-async-with-postgresql_adminer_1 ... done
Recreating fastapi-async-with-postgresql_db_1    ... done
```

### Check postgresql

You can check if the stack is up and running :

```shell
$ docker-compose ps
                 Name                                Command               State           Ports
---------------------------------------------------------------------------------------------------------
fastapi-async-with-postgresql_adminer_1   entrypoint.sh docker-php-e ...   Up      0.0.0.0:8080->8080/tcp
fastapi-async-with-postgresql_db_1        docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp
```

### Run a psql client

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

### Or... use adminer

`docker-compose.yml` file runs [adminer](https://www.adminer.org), a great php tool for db navigation.

You should open the
url [http://localhost:8080/?pgsql=db&username=vincent&db=vincent&ns=public&select=notes](http://localhost:8080/?pgsql=db&username=vincent&db=vincent&ns=public&select=notes)

Adminer will display the content of the "notes" table that the project uses.

![adminer]

---

## Run the server

You can start the server with `make run`

```shell
$ make run
2020-12-30 10:17:42,350:INFO:db_utils:Defining configuration for db at [postgresql://vincent:****@localhost:5432/vincent?sslmode=prefer]
2020-12-30 10:17:42,423:INFO:schema:Defining table 'notes'
2020-12-30 10:17:42,424:INFO:schema:Creating schema
2020-12-30 10:17:42,614 INFO sqlalchemy.engine.base.Engine select version()
2020-12-30 10:17:42,614:INFO:sqlalchemy.engine.base.Engine:select version()
2020-12-30 10:17:42,614 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:42,614:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:42,616 INFO sqlalchemy.engine.base.Engine select current_schema()
2020-12-30 10:17:42,616:INFO:sqlalchemy.engine.base.Engine:select current_schema()
2020-12-30 10:17:42,617 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:42,617:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:42,619 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:42,619:INFO:sqlalchemy.engine.base.Engine:SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:42,619 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:42,619:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:42,620 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:42,620:INFO:sqlalchemy.engine.base.Engine:SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:42,620 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:42,620:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:42,620 INFO sqlalchemy.engine.base.Engine show standard_conforming_strings
2020-12-30 10:17:42,620:INFO:sqlalchemy.engine.base.Engine:show standard_conforming_strings
2020-12-30 10:17:42,621 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:42,621:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:42,622 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2020-12-30 10:17:42,622:INFO:sqlalchemy.engine.base.Engine:select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2020-12-30 10:17:42,622 INFO sqlalchemy.engine.base.Engine {'name': 'notes'}
2020-12-30 10:17:42,622:INFO:sqlalchemy.engine.base.Engine:{'name': 'notes'}
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
2020-12-30 10:17:42,639:INFO:uvicorn.error:Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [8791] using statreload
2020-12-30 10:17:42,639:INFO:uvicorn.error:Started reloader process [8791] using statreload
2020-12-30 10:17:43,137:INFO:db_utils:Defining configuration for db at [postgresql://vincent:****@localhost:5432/vincent?sslmode=prefer]
2020-12-30 10:17:43,228:INFO:schema:Defining table 'notes'
2020-12-30 10:17:43,233:INFO:schema:Creating schema
2020-12-30 10:17:43,300 INFO sqlalchemy.engine.base.Engine select version()
2020-12-30 10:17:43,300:INFO:sqlalchemy.engine.base.Engine:select version()
2020-12-30 10:17:43,300 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:43,300:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:43,305 INFO sqlalchemy.engine.base.Engine select current_schema()
2020-12-30 10:17:43,305:INFO:sqlalchemy.engine.base.Engine:select current_schema()
2020-12-30 10:17:43,306 INFO sqlalchemy.engine.base.Engine {}
2020-12-30 10:17:43,306:INFO:sqlalchemy.engine.base.Engine:{}
2020-12-30 10:17:43,309 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:43,309:INFO:sqlalchemy.engine.base.Engine:SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2020-12-30 10:17:43,309 INFO sqlalchemy.engine.base.Engine {}

```

### Using poetry runner

You can prefer to launch the server through poetry runner :

```shell
poetry run python src/main.py

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

### Stop the server

You can stop the server by hitting 'Ctrl' + 'C'

```shell
^CINFO:     Shutting down
2020-12-30 10:26:11,615:INFO:uvicorn.error:Shutting down
INFO:     Waiting for application shutdown.
2020-12-30 10:26:11,718:INFO:uvicorn.error:Waiting for application shutdown.
2020-12-30 10:26:11,728:INFO:databases:Disconnected from database postgresql://vincent:********@localhost:5432/vincent?sslmode=prefer
INFO:     Application shutdown complete.
2020-12-30 10:26:11,730:INFO:uvicorn.error:Application shutdown complete.
INFO:     Finished server process [8797]
2020-12-30 10:26:11,730:INFO:uvicorn.error:Finished server process [8797]
INFO:     Stopping reloader process [8791]
2020-12-30 10:26:11,895:INFO:uvicorn.error:Stopping reloader process [8791]

```

---

## API Documentation

API's documentation is autogenerated with the help of FastAPI framework.

FastAPI build automagicaly an [OpenAPI v3](https://swagger.io/specification/) documentation JSON file that is served
with a local Web site at [http://localhost:5000/docs](http://localhost:5000/docs).

![openapi]

It also provides the excellent [redoc](https://github.com/Redocly/redoc) that present ths OpenAPI v3 in a very neat way
at [http://localhost:5000/redoc](http://localhost:5000/redoc).

![redoc]

This documentation is incredibly useful when you have to verify your API endpoints during development.


---

## Test the server

You can use curl or whatever client for REST API

Create a Note :

```bash
$ curl -i -X POST http://localhost:5000/notes --data "{\"text\":\"Test\",\"completed\":\"false\"}"
HTTP/1.1 200 OK
date: Tue, 29 Dec 2020 20:25:46 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"text":"Test","completed":false,"id":1}%
```

Request all notes :

```shell
curl -i -X GET http://localhost:5000/notes
HTTP/1.1 200 OK
date: Tue, 29 Dec 2020 20:26:36 GMT
server: uvicorn
content-length: 42
content-type: application/json

[{"id":1,"text":"Test","completed":false}]%
```

---

## Run integration tests

Once you have your database up and running you should be able to launche all the test with one command with the help of
the Makefile command `make tests`.

```shell
$ make tests
===================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.9.1, pytest-5.4.3, py-1.10.0, pluggy-0.13.1 -- /Users/vdagoury/Library/Caches/pypoetry/virtualenvs/api-sK0lnS2G-py3.9/bin/python
cachedir: .pytest_cache
rootdir: /Users/vdagoury/Projects/Python/asynchronous/fastapi-async-with-postgresql
collected 11 items                                                                                                                                                                             

src/tests/test_api.py::test_version PASSED
src/tests/test_api.py::test_create_note PASSED
src/tests/test_api.py::test_known_note PASSED
src/tests/test_api.py::test_get_all_notes PASSED
src/tests/test_api.py::test_update_note PASSED
src/tests/test_api.py::test_get_notes PASSED
src/tests/test_api.py::test_get_notes_with_pagination [{'id': 1, 'text': 'test', 'completed': False}]
PASSED
src/tests/test_api.py::test_delete_note PASSED
src/tests/test_api.py::test_unknown_note PASSED
src/tests/test_api.py::test_create_another_note PASSED
src/tests/test_api.py::test_get_one_note PASSED

====================================================================================== 11 passed in 0.18s ======================================================================================

```

!!! Note

    You may need to drop the table with `drop table notes;` 
    in order to find proper starting conditions for integration tests.

    I probably need to go further for initial state creation for this integrations tests. 

---

## Run load tests

The project uses [locust](https://locust.io) with a single load test file that you can easily update.

![locust]

```shell
$ make load_tests
[2020-12-29 21:55:19,670] yourmachine.local/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2020-12-29 21:55:19,678] yourmachine.local/INFO/locust.main: Starting Locust 1.4.1
[2020-12-29 21:56:09,048] yourmachine.local/INFO/locust.runners: Spawning 10 users at the rate 2 users/s (0 users already running)...
[2020-12-29 21:56:13,564] yourmachine.local/INFO/locust.runners: All users spawned: QuickstartUser: 10 (10 total running)

```

You're invited to open the given http://0.0.0.0:8089

Then you should be able to input a setting.

![locust dialog]

The test begins when you hit the button :

![locust test tab]

You find charts that show the global performance all along tht test

![locust charts]

After a few minutes you should get something like this

![locust charts 2]

You can stop the load testing by pressing Ctrl+C which will give you an output on the temrinal like this one :

```shell
[...]
2020-12-30T20:43:03Z <Greenlet at 0x1117bf6a0: run_user(<locustfile.QuickstartUser object at 0x111817ca0>)> failed with KeyboardInterrupt

[2020-12-30 21:43:03,026] yourmachine.local/INFO/locust.main: Running teardowns...
[2020-12-30 21:43:03,026] yourmachine.local/INFO/locust.main: Shutting down (exit code 1), bye.
[2020-12-30 21:43:03,026] yourmachine.local/INFO/locust.main: Cleaning up runner...
[2020-12-30 21:43:03,026] yourmachine.local/INFO/locust.runners: Stopping 2 users
[2020-12-30 21:43:03,027] yourmachine.local/INFO/locust.runners: 2 Users have been stopped, 0 still running
 Name                                                          # reqs      # fails  |     Avg     Min     Max  Median  |   req/s failures/s
--------------------------------------------------------------------------------------------------------------------------------------------
 POST /notes                                                        2     0(0.00%)  |      19      14      23      15  |    0.03    0.00
 GET /notes/1                                                    2806 2806(100.00%)  |       4       3      17       4  |   45.28   45.28
 GET /notes/10                                                   2804 2804(100.00%)  |       4       3      15       4  |   45.25   45.25
 GET /notes/2                                                    2806     0(0.00%)  |       4       3      12       4  |   45.28    0.00
 GET /notes/3                                                    2806     0(0.00%)  |       4       3      29       4  |   45.28    0.00
 GET /notes/4                                                    2806     0(0.00%)  |       4       3      13       4  |   45.28    0.00
 GET /notes/5                                                    2806     0(0.00%)  |       4       3      15       4  |   45.28    0.00
 GET /notes/6                                                    2805    23(0.82%)  |       4       3      10       4  |   45.26    0.37
 GET /notes/7                                                    2805 2805(100.00%)  |       4       3      11       4  |   45.26   45.26
 GET /notes/8                                                    2804 2804(100.00%)  |       4       3      15       4  |   45.25   45.25
 GET /notes/9                                                    2804 2804(100.00%)  |       4       3      26       4  |   45.25   45.25
--------------------------------------------------------------------------------------------------------------------------------------------
 Aggregated                                                     28054 14046(50.07%)  |       4       3      29       4  |  452.69  226.65

Response time percentiles (approximated)
 Type     Name                                                              50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 POST     /notes                                                             23     23     23     23     23     23     23     23     23     23     23      2
 GET      /notes/1                                                            4      4      4      5      5      5      6      7     10     17     17   2806
 GET      /notes/10                                                           4      4      4      5      5      5      6      7     12     15     15   2804
 GET      /notes/2                                                            4      4      4      5      5      5      6      7     10     13     13   2806
 GET      /notes/3                                                            4      4      4      5      5      5      6      7     12     30     30   2806
 GET      /notes/4                                                            4      4      4      5      5      5      6      6     13     14     14   2806
 GET      /notes/5                                                            4      4      4      5      5      5      6      7     14     16     16   2806
 GET      /notes/6                                                            4      4      4      5      5      5      6      7      9     11     11   2805
 GET      /notes/7                                                            4      4      4      5      5      5      6      7      9     12     12   2805
 GET      /notes/8                                                            4      4      4      5      5      5      6      7     11     16     16   2804
 GET      /notes/9                                                            4      4      4      5      5      5      6      7     10     26     26   2804
--------|------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 None     Aggregated                                                          4      4      4      5      5      5      6      7     10     23     30  28054

Error report
 # occurrences      Error                                                                                               
--------------------------------------------------------------------------------------------------------------------------------------------
 2806               GET /notes/1: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/1')       
 23                 GET /notes/6: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/6')       
 2805               GET /notes/7: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/7')       
 2804               GET /notes/8: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/8')       
 2804               GET /notes/9: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/9')       
 2804               GET /notes/10: HTTPError('404 Client Error: Not Found for url: http://localhost:5000/notes/10')     
--------------------------------------------------------------------------------------------------------------------------------------------

make: *** [load_tests] Error 1


```

---

## mkdocs

This site hase been generated with the help of [mkdocs.org](https://www.mkdocs.org) and the incredible theme (much more
than that actually) [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).


### Basics : mkdocs Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

### Documentation : layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

### Run documentation server

You can use `make serve` to start the documentation server :

```shell
$ make serve
INFO    -  Building documentation... 
INFO    -  Cleaning site directory 
INFO    -  Documentation built in 0.10 seconds 
[I 201230 22:19:08 server:335] Serving on http://127.0.0.1:8000
INFO    -  Serving on http://127.0.0.1:8000
[I 201230 22:19:08 handlers:62] Start watching changes
INFO    -  Start watching changes
[I 201230 22:19:08 handlers:64] Start detecting changes
INFO    -  Start detecting changes
[I 201230 22:19:11 handlers:135] Browser Connected: http://127.0.0.1:8000/#objectives
INFO    -  Browser Connected: http://127.0.0.1:8000/#objectives
```

You should see the documentation at [http://127.0.0.1:8000](http://127.0.0.1:8000)

![documentation]

----


[documentation]: img/documentation.png

[adminer]: img/adminer.png

[locust]: img/locust_logo.png

[locust dialog]: img/locust_dialog.png

[locust test tab]: img/locust_launch_tab.png

[locust charts]: img/locust_charts.png

[locust charts 2]: img/locust_charts_2.png

[openapi]: img/openapi.png

[redoc]: img/redoc.png
