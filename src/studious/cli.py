"""Command-line interface for the project."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A basic Python project")
    parser.add_argument(
        "--name",
        defaul

def main() -> None:
    args = build_parser().parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
