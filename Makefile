.PHONY: fmt init test typecheck new

.DEFAULT_GOAL := help


## Initialise/sync the virtualenv
init:
	uv sync

## Run autoformatters
fmt:
	uv run ruff check --fix
	uv run ruff format

## Run tests
test:
	uv run pytest

## Run typechecker
typecheck:
	uv run mypy

## Create a blank solution template for a specific day
new:
	./new.sh


## Display this help message
help:
	@echo "$$(tput setaf 2)Available rules:$$(tput sgr0)";sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## /---/;td" -e"s/:.*//;G;s/\\n## /===/;s/\\n//g;p;}" ${MAKEFILE_LIST}|awk -F === -v n=$$(tput cols) -v i=4 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"- %s%s%s\n",a,$$1,z;m=split($$2,w,"---");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;}printf"%*s%s\n",-i," ",w[j];}}'