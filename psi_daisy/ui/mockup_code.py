# ################################
# File:     mockup_code.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI MockupCode component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Pre
from ..utils import merge_classes

def MockupCode(*lines, **kw):
    """DaisyUI code mockup. lines are (prefix, code) tuples or strings."""
    user_cls = kw.pop("cls", None)
    def make(ln):
        if isinstance(ln, tuple): return Pre(data_prefix=ln[0])(ln[1])
        return Pre(ln)
    return Div(*[make(l) for l in lines], cls=merge_classes("mockup-code", user_cls), **kw)
