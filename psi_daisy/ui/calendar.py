# ################################
# File:     calendar.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Calendar component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260623, fix calendar. use cally. use FastHTML's generic tag ft_hx 
#   * version, who, when, why
# ################################

from fasthtml.common import ft_hx
from ..utils import merge_classes


def Calendar(**kw):
    """DaisyUI calendar component using Cally web components."""
    user_cls = kw.pop("cls", None)

    return ft_hx(
        "calendar-date",
        ft_hx("calendar-month"),
        cls=merge_classes("cally", user_cls),
        **kw, )
