# ################################
# File:     dropdown.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Dropdown component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * 001, luch, 260705, added orientation
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Ul
from ..utils import merge_classes
from .types import Position, Orientation 


def Dropdown(trigger, *items, position:Position="bottom", orientation:Orientation="vertical", menu_cls:str|None=None, menu_kw:dict|None=None, **kw):
    """DaisyUI dropdown component."""
    menu_kw = menu_kw or {}
    pos_cls = dict(bottom="dropdown-bottom", top="dropdown-top", left="dropdown-left", right="dropdown-right").get(position, "dropdown-bottom")
    orient_cls = dict(vertical="menu-vertical flex flex-col flex-nowrap overflow-y-auto overflow-x-hidden", horizontal="menu-horizontal flex flex-row flex-nowrap overflow-x-auto overflow-y-hidden").get(orientation, "menu-vertical flex flex-col flex-nowrap overflow-y-auto overflow-x-hidden")
    user_cls = kw.pop("cls", None)
    menu_cls = merge_classes(f"dropdown-content menu {orient_cls} bg-base-100 rounded-box z-1 w-52 max-h-32 p-2 shadow-sm", menu_cls)
    return Div(trigger, Ul(*items, cls=menu_cls, **menu_kw), cls=merge_classes(f"dropdown {pos_cls}", user_cls), **kw)
