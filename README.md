# aoc
My solutions to Advent of Code

https://adventofcode.com/


## First time setup

Run `poetry install` to install all dependencies.

Nb. this Requires [Poetry](https://python-poetry.org/) itself to be installed first.


## Running

On the first run of each day's solution, `aoc` will pull your user input directly from the Advent of Code website, using a session cookie you specify. The input is cached for use in subsequent runs.

You will be prompted to enter your session cookie if no current cookie is stored, or the currently stored cookie is invalid.

### Today's problem
```shell
poetry run aoc
```
Note: this only works between the 1st and 25th December.

### An arbitrary problem from the most recent AOC
For example, day 6:
```shell
poetry run aoc 6
```

### An arbitrary problem from a specific year:
For example, 2015 day 21:
```shell
poetry run -y 2015 21
```

### Extra options
For additional options, see
```shell
poetry run aoc --help
```