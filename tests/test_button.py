import pytest

from studious.button import Button


def test_button_renders_label() -> None:
    assert Button("Save").render() == "[Save]"


def test_disabled_button_renders_and_does_not_call_action() -> None:
    called = False

    def action() -> None:
        nonlocal called
        called = True

    button = Button("Save", on_click=action, disabled=True)

    assert button.render() == "[Save] (disabled)"
    assert button.click() is False
    assert called is False


def test_enabled_button_calls_action() -> None:
    calls = []
    button = Button("Save", on_click=lambda: calls.append("saved"))

    assert button.click() is True
    assert calls == ["saved"]


@pytest.mark.parametrize("label", ["", "   "])
def test_button_rejects_empty_label(label: str) -> None:
    with pytest.raises(ValueError, match="button label"):
        Button(label)
