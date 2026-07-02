# ################################
# File:     toast.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Toast component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import ToastPos, ToastVPos

def Toast(*children, h: ToastPos = "end", v: ToastVPos = "bottom", **kw):
    """DaisyUI toast container component."""
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes(f"toast toast-{h} toast-{v}", user_cls), **kw)
