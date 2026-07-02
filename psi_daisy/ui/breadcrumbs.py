# ################################
# File:     breadcrumbs.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Breadcrumbs component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Ul, Li, A
from ..utils import merge_classes

def Breadcrumbs(*items, **kw):
    """DaisyUI breadcrumbs. items are (label, href) tuples or strings."""
    user_cls = kw.pop("cls", None)
    def make(it):
        if isinstance(it, tuple): return Li(A(it[0], href=it[1]))
        return Li(it)
    return Div(Ul(*[make(i) for i in items]), cls=merge_classes("breadcrumbs text-sm", user_cls), **kw)
