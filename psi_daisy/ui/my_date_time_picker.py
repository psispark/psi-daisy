# ################################
# File:     my_date_time_picker.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Date Time Picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260628, build
# ################################

from typing import Any
from fasthtml.common import Div
from ..utils import merge_classes
from .my_date_picker import MyDatePicker
from .my_time_picker import MyTimePicker
from .types import Color, Size, SelectVariant


def MyDateTimePicker(name: str = "datetime", 
        year: int = 2026, month: int = 1, day: int = 1, start_year: int = 1900, end_year: int = 2100, 
        hour: int = 0, minute: int = 0, second: int = 0, 
        color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", 
        date_kw: dict[str, Any] | None = None, time_kw: dict[str, Any] | None = None, **kw):
    "Custom my-date-time-picker component."
    user_cls = kw.pop("cls", None)
    date_kw, time_kw = date_kw or {}, time_kw or {}
    return Div(
        MyDatePicker(name=name, year=year, month=month, day=day, start_year=start_year, end_year=end_year, color=color, size=size, variant=variant, **date_kw),
        MyTimePicker(name=name, hour=hour, minute=minute, second=second, color=color, size=size, variant=variant, **time_kw),
        cls=merge_classes("flex flex-col gap-4", user_cls),
        **kw)
