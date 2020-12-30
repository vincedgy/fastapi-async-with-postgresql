# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help install test run

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# Server status evaluation
SERVER_PID := $(shell sh -c "ps | grep -v grep | grep 'src/main.py' | head -1 | cut -d \t -f1")
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
	@echo "---------------HELP-----------------"
	@echo "- Setup the project : make install"
	@echo "- Run the server (blocking):  make start"
	@echo "- Evaluate status of the server :  make status"
	@echo "- Stop (killp) the server :  make kill"
	@echo "- Run tests on a running server: make tests"
	@echo "------------------------------------"

install:
	@poetry install

status:
	@date
	@echo "Running status of server is $(SERVER_RUNNING)"
	@echo "Running status of child runners is $(HAVE_CHILD)"

do_stop_server:
	@-kill -9 $(SERVER_PID)
do_stop_children:
	@-kill -9 $(CHILD_PID)
kill: status do_stop_server do_stop_children
	@echo "Killing server on PID $(SERVER_PID) and children on PID $(CHILD_PID)"
	@-lsof -i tcp:5000

tail:
	@tail run.log

do_start:
	@poetry run python src/main.py >run.log 2>&1 &
	@$(shell sleep 3)
start: do_start
	@echo Check run.log for logging


tests: install
	@poetry run pytest

serve:
	@poetry run mkdocs serve

publish:
	@poetry run mkdocs gh-deploy

