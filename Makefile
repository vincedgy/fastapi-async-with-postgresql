# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help install test run

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# Server status evaluation
SERVER_PID := $(shell sh -c "ps | grep -v grep | grep 'main.py' | head -1 | cut -d \t -f1")
ifeq ('$(strip $(SERVER_PID))','')
		SERVER_RUNNING=FALSE
else
		SERVER_RUNNING=TRUE
endif

CHILD_PID := $(shell sh -c "ps -ax | grep -i spawn_main | grep -v grep | cut -d ' ' -f1")
ifeq ('$(strip $(CHILD_PID))','')
		HAVE_CHILD=FALSE
else
		HAVE_CHILD=TRUE
endif


# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@date
	@echo "                                   \n\
   __  __     ______     __         ______    \n\
  /\ \_\ \   /\  ___\   /\ \       /\  == \   \n\
  \ \  __ \  \ \  __\   \ \ \____  \ \  _-/   \n\
   \ \_\ \_\  \ \_____\  \ \_____\  \ \_\     \n\
    \/_/\/_/   \/_____/   \/_____/   \/_/     \n"
	@echo "---------------HELP------------------------------------"
	@echo "- Setup the project              : make install"
	@echo "- Run the server (blocking)      : make start"
	@echo "- Evaluate status of the server  : make status"
	@echo "- Stop (kill) the server         : make kill"
	@echo "- Tail the current log file      : make tail"
	@echo "- Run tests on a running server  : make tests"
	@echo "- Run tests on a running server  : make load_tests"
	@echo "- Launch mkdocs server Run       : make serve"
	@echo "- Publish docs GitHub pages      : make publish"
	@echo "--------------------------------------------------------"
	@echo Enjoy 🍺 !

install:
	@poetry install

status:
	@date
	@echo "Running status of server is $(SERVER_RUNNING)"
	@echo "Running status of child runners is $(HAVE_CHILD)"

kill: status
	@echo "Killing process $(SERVER_PID)"
	@-kill -9 $(SERVER_PID)
	@sleep 1
	@echo "Killing process $(CHILD_PID)"
	@-kill -9 $(CHILD_PID)
	@sleep 1
	@echo "Killing server on PID $(SERVER_PID) and children on PID $(CHILD_PID)"
	@-lsof -i tcp:5000

tail:
	@tail run.log

do_start:
	@poetry run python src/main.py >run.log 2>&1 &
	@$(shell sleep 3)
start: do_start
	@echo Check run.log for logging

run:
	@poetry run python src/main.py

tests:
	@poetry run pytest -sv

load_tests:
	@poetry run locust -f ./locust/locustfile.py

serve:
	@poetry run mkdocs serve

publish:
	@poetry run mkdocs gh-deploy

