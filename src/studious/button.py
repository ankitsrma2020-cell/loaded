"""A small, dependency-free button component for terminal applications."""

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Button:
    """Represent a labeled action that can be triggered from Python code.

    Example::

        save_button = Button("Save", on_click=lambda: print("Saved!"))
        save_button.click()
    """

    label: str
    on_click: Optional[Callable[[], None]] = None
    disabled: bool = False

    def __post_init__(self) -> None:
        if not self.label.strip():
            raise ValueError("button label must not be empty")

    def click(self) -> bool:
        """Run the button action; return whether it was enabled and triggered."""
        if self.disabled:
            return False
        if self.on_click is not None:
            self.on_click()
        return True

    def render(self) -> str:
        """Return a simple text representation of the button."""
        label = f"[{self.label}]"
        return f"{label} (disabled)" if self.disabled else label
