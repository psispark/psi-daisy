# ################################
# File:     mask.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Mask component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import MaskShape

def Mask(*children, shape: MaskShape = "squircle", **kw):
    """DaisyUI mask component."""
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes(f"mask mask-{shape}", user_cls), **kw)
