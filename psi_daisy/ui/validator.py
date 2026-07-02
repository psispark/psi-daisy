# ################################
# File:     validator.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Validator component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Validator(*children, **kw):
    """DaisyUI validator wrapper component."""
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes("validator", user_cls), **kw)
