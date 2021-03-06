### Hexlet tests and linter status:
[![Actions Status](https://github.com/SoulH0unD/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/SoulH0unD/python-project-lvl2/actions)
[![Linter](https://github.com/SoulH0unD/python-project-lvl2/actions/workflows/linter.yml/badge.svg)](https://github.com/SoulH0unD/python-project-lvl2/actions/workflows/linter.yml)
[![Test](https://github.com/SoulH0unD/python-project-lvl2/actions/workflows/test.yml/badge.svg)](https://github.com/SoulH0unD/python-project-lvl2/actions/workflows/test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/87dd5a23cf3d8c233100/maintainability)](https://codeclimate.com/github/SoulH0unD/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/87dd5a23cf3d8c233100/test_coverage)](https://codeclimate.com/github/SoulH0unD/python-project-lvl2/test_coverage)

## Generate diff.
Command line tool for generating difference between two configuration files.

## Features
* Suppported formats: YAML, JSON
* Report generation as plain text, structured text or JSON
* Can be used as CLI tool or external library

## How to Install and run package.
```
pip install git+https://github.com/SoulH0unD/python-project-lvl2
```
## Usage
```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```


Flat File Comparison (JSON)
[![asciicast](https://asciinema.org/a/VohM6vMH7y2mfwqFnBZV6kegT.svg)](https://asciinema.org/a/VohM6vMH7y2mfwqFnBZV6kegT)
Flat File Comparison (YAML)
[![asciicast](https://asciinema.org/a/6ZpwxAo9v6AinCKCMWGAWaJBE.svg)](https://asciinema.org/a/6ZpwxAo9v6AinCKCMWGAWaJBE)
Comparison of nested files and format output stylish(JSON and YAML)
[![asciicast](https://asciinema.org/a/0i2I3ABll1r0pb4eIqdCJPNVJ.svg)](https://asciinema.org/a/0i2I3ABll1r0pb4eIqdCJPNVJ)
Comparison of nested files and format output plain(JSON and YAML)
[![asciicast](https://asciinema.org/a/VZZdqCr9Jyd97lAFD507OpSaV.svg)](https://asciinema.org/a/VZZdqCr9Jyd97lAFD507OpSaV)
Comparison of nested files and format output json(JSON and YAML)
[![asciicast](https://asciinema.org/a/NjT9genK6dcIVO8WLq8JzHmQB.svg)](https://asciinema.org/a/NjT9genK6dcIVO8WLq8JzHmQB)