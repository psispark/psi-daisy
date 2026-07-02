# ################################
# File:     my_color_picker.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Build a color picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260630, build
# ################################

import re
from matplotlib.colors import CSS4_COLORS
from fasthtml.common import Div, Span, Code 
from . import Input, Label
from ..themes import hex_to_rgb, hex_to_oklch
from .types import WebColor
from ..utils import merge_classes


def valid_hex(o:str|None) -> bool: return bool(o and re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", o))


def color_name(hex_color:str) -> str:
    hits = [k for k,v in CSS4_COLORS.items() if v.lower()==hex_color.lower()]
    return hits[0] if hits else ""


def MyColorPicker(name:str="color", web_color:WebColor="dodgerblue", hex_color:str|None=None, label:str|None="Color", show_outputs:bool=False, input_kw:dict|None=None, **kw):
    "Color picker component."
    user_cls = kw.pop("cls", None)
    input_kw = input_kw or {}
    hex_val = hex_color.lower() if valid_hex(hex_color) else CSS4_COLORS.get(web_color, CSS4_COLORS["dodgerblue"]).lower()
    nm, rgb, oklch = color_name(hex_val), hex_to_rgb(hex_val), hex_to_oklch(hex_val)
    outs = Div(
        Code(f"web: {nm}", cls="text-xs text-base-content/60", data_color_name=True),
        Code(f"rgb: {rgb}", cls="text-xs text-base-content/60", data_color_rgb=True),
        Code(f"hex: {hex_val}", cls="text-xs text-base-content/60", data_color_hex=True),
        Code(f"oklch: {oklch}", cls="text-xs text-base-content/60", data_color_oklch=True),
        cls="flex flex-col gap-1")
    inp = Input(type="color", name=name, value=hex_val, cls="w-14 h-10 cursor-pointer rounded border-0 p-0", onchange="psiUpdateColorPicker(this)", **input_kw)
    body = Div(inp, outs, cls="flex items-start gap-3") if show_outputs else Div(inp, cls="flex items-start gap-3")
    return Div(Label(Span(label), cls="label") if label else None, body, data_color_picker=True, cls=merge_classes("flex flex-col gap-1", user_cls), **kw)
