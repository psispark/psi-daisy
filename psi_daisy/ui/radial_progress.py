# ################################
# File:     radial_progress.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI RadialProgress component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Color

def RadialProgress(value: int = 0, *, color: Color = "primary", **kw):
    """DaisyUI radial progress component."""
    user_cls = kw.pop("cls", None)
    return Div(f"{value}%", style=f"--value:{value};",
               role="progressbar", cls=merge_classes(f"radial-progress text-{color}", user_cls), **kw)
