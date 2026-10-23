from studious.cli import build_parser, main


def test_default_name() -> None:
    args = build_parser().parse_args([])
    assert args.name == "world"


def test_custom_name() -> None:
    args = build_parser().parse_args(["--name", "Ada"])
    assert args.name == "Ada"


def test_main_prints_greeting(monkeypatch, capsys) -> None:
   