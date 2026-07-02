# ################################
# File:     my_time_picker.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Time Picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260628, build
# ################################

from typing import Any
from fasthtml.common import Div
from ..utils import merge_classes
from ._picker import picker_select
from .types import Color, Size, SelectVariant


def MyTimePicker(name: str = "time", hour: int = 0, minute: int = 0, second: int = 0, 
        color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", 
        hour_kw: dict[str, Any] | None = None, minute_kw: dict[str, Any] | None = None, second_kw: dict[str, Any] | None = None, **kw):
    "Custom my-time-picker component."
    user_cls = kw.pop("cls", None)
    hour_kw, minute_kw, second_kw = hour_kw or {}, minute_kw or {}, second_kw or {}
    return Div(
        picker_select("Hour", f"{name}_hour", range(24), hour, 2, color=color, size=size, variant=variant, select_kw=hour_kw),
        picker_select("Minute", f"{name}_minute", range(60), minute, 2, color=color, size=size, variant=variant, select_kw=minute_kw),
        picker_select("Second", f"{name}_second", range(60), second, 2, color=color, size=size, variant=variant, select_kw=second_kw),
        cls=merge_classes("flex gap-3", user_cls),
        **kw)
