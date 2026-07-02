# ################################
# File:     my_lucide_icon.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Build Lucide icon component.
# Release:  v0.2
# History:
#   * 001, luch, 260624, build
# ################################

import re
from fasthtml.common import I
from ..utils import merge_classes
from .types import Color 


def MyLucideIcon(
    icon: str = "lightbulb",
    color: Color = "primary",
    size: int = 24,
    stroke_width: float = 3,
    hex_color:str|None=None, 
    **kw,
):
    """Lucide icon component."""
    user_cls = kw.pop("cls", None)
    parts = [f"text-{color}"]
    if hex_color and not re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hex_color): hex_color = None

    if hex_color: return I(data_lucide=icon, color=hex_color, width=size, height=size, stroke_width=stroke_width, cls=user_cls, **kw)
    return I(data_lucide=icon, width=size, height=size, stroke_width=stroke_width, cls=merge_classes(f"text-{color}", user_cls), **kw)
    