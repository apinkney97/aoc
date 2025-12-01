.DEFAULT_GOAL := help


.PHONY: init
## Initialise/sync the virtualenv
init:
	uv sync

.PHONY: fmt
## Run autoformatters
fmt:
	uv run ruff check --fix
	uv run ruff format

.PHONY: test
## Run tests
test:
	uv run pytest

.PHONY: coverage
## Run tests with coverage
coverage:
	uv run pytest -xvv --cov aoc/utils --cov-report term-missing:skip-covered --cov-report html:cov_html

.PHONY: view-cov
## View coverage report in browser
view-cov:
	xdg-open cov_html/index.html

.PHONY: typecheck
## Run typechecker
typecheck:
	uv run mypy

.PHONY: new
## Create a blank solution template for a specific day
new:
	./new.sh


.PHONY: help
## Display this help message
help:
	@echo "$$(tput setaf 2)Available rules:$$(tput sgr0)";sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## /---/;td" -e"s/:.*//;G;s/\\n## /===/;s/\\n//g;p;}" ${MAKEFILE_LIST}|awk -F === -v n=$$(tput cols) -v i=4 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"- %s%s%s\n",a,$$1,z;m=split($$2,w,"---");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;}printf"%*s%s\n",-i," ",w[j];}}'