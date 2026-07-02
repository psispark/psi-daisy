# ################################
# File:     my_date_picker.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Date Picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260628, build
# ################################

from typing import Any
from calendar import monthrange
from fasthtml.common import Div
from ..utils import merge_classes
from ._picker import picker_select
from .types import Color, Size, SelectVariant


def MyDatePicker(name: str = "date", year: int = 2026, month: int = 1, day: int = 1, start_year: int = 1900, end_year: int = 2100, 
        color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", 
        year_kw: dict[str, Any] | None = None, month_kw: dict[str, Any] | None = None, day_kw: dict[str, Any] | None = None, **kw):
    "Custom my-date-picker component."
    user_cls = kw.pop("cls", None)
    year_kw, month_kw, day_kw = year_kw or {}, month_kw or {}, day_kw or {}
    year_kw = dict(year_kw, id=f"{name}_year", data_date_part="year", onchange="psiUpdateDatePicker(this)")
    month_kw = dict(month_kw, id=f"{name}_month", data_date_part="month", onchange="psiUpdateDatePicker(this)")
    day_kw = dict(day_kw, id=f"{name}_day", data_date_part="day")

    year = min(max(year, start_year), end_year)
    month = min(max(month, 1), 12)
    max_day = monthrange(year, month)[1]
    day = min(max(day, 1), max_day)

    return Div(
        picker_select("Year", f"{name}_year", range(start_year, end_year+1), year, color=color, size=size, variant=variant, select_kw=year_kw),
        picker_select("Month", f"{name}_month", range(1, 13), month, 2, color=color, size=size, variant=variant, select_kw=month_kw),
        picker_select("Day", f"{name}_day", range(1, max_day+1), day, 2, color=color, size=size, variant=variant, select_kw=day_kw),
        data_date_picker=name,
        cls=merge_classes("flex gap-3", user_cls),
        **kw)
