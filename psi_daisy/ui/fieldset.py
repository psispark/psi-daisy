# ################################
# File:     fieldset.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Fieldset component.
# Release:  v0.1
# History:
#   * 001, Luch, 260531, build
#   * version, who, when, why
# ################################

from fasthtml.common import Fieldset as FHFieldset, Legend, Div
from ..utils import merge_classes

def Fieldset(legend: str, *children, hint: str = "", **kw):
    """DaisyUI fieldset component."""
    user_cls = kw.pop("cls", None)
    return FHFieldset(
        Legend(legend, cls="fieldset-legend"),
        *children,
        *([Div(hint, cls="fieldset-label")] if hint else []),
        cls=merge_classes("fieldset bg-base-200 border border-base-300 p-4 rounded-box", user_cls), **kw)
