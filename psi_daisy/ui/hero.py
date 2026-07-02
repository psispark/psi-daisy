# ################################
# File:     hero.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Hero component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Hero(*children, **kw):
    """DaisyUI hero component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(*children, cls="hero-content text-center"),
               cls=merge_classes("hero min-h-screen bg-base-200", user_cls), **kw)
