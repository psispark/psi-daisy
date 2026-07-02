# ################################
# File:     theme_controller.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI ThemeController component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Input
from ..utils import merge_classes

def ThemeController(theme: str, **kw):
    """DaisyUI theme controller (checkbox input that sets data-theme)."""
    user_cls = kw.pop("cls", None)
    return Input(type="checkbox", value=theme, cls=merge_classes("theme-controller", user_cls), **kw)
