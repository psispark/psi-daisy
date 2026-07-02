# ################################
# File:     button.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Button component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260621, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Button as FHButton
from ..utils import merge_classes
from .types import Color, Size, ButtonVariant


def Button(
    label: str,
    *,
    color: Color = "primary",
    size: Size = "md",
    variant: ButtonVariant = "",
    **kw,
):
    """DaisyUI Button component."""
    parts = ["btn", f"btn-{color}"]
    if variant: parts.append(f"btn-{variant}")
    size_map = {"xs": "btn-xs", "sm": "btn-sm", "md": "", "lg": "btn-lg"}
    if s := size_map.get(size, ""): parts.append(s)

    user_cls = kw.pop("cls", None)
    return FHButton(label, cls=merge_classes(" ".join(parts), user_cls), **kw)
