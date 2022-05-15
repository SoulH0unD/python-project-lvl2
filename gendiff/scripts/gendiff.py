#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.lib.cli import cli


def main():
    args = cli()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
