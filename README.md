# advent

My solutions for the [Advent of Code](https://adventofcode.com/) problems.

**Table of Contents**

- [Prerequisites](#prerequisites)
- [Conventions](#conventions)
- [Installation](#installation)
- [Running Solutions](#running-solutions)
- [Testing](#testing)

## Prerequisites

- Python 3 (https://www.python.org/)

## Conventions

My solutions aim to have minimal package dependencies and aim to adhere to PEP8
using the [`pycodestyle`](https://github.com/pycqa/pycodestyle) style checker.

## Installation

```bash
git clone https://github.com/erictleung/advent.git
cd advent
python setup.py install
```

## Running Solutions

Here is an example solution run.

```bash
cd advent
python advent2015/not_quite_lisp.py data/2015_day1.txt
```

The data is saved and run through as a command line interface.

## Testing

```bash
git clone https://github.com/erictleung/advent.git
cd advent
python -m unittest
python -m unittest -v # See tests being run
```
