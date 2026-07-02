# ################################
# File:     steps.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Steps component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Ul, Li
from ..utils import merge_classes
from .types import Color, Orientation

def Steps(*labels, color: Color = "primary", orientation: Orientation = "horizontal", **kw):
    """DaisyUI steps component."""
    root = "steps"
    if orientation == "vertical": root += " steps-vertical"
    user_cls = kw.pop("cls", None)
    return Ul(*[Li(label, cls=f"step step-{color}") for label in labels],
              cls=merge_classes(root, user_cls), **kw)
