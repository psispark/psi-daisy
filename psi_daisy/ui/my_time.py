# ################################
# File:     my_time.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Time Picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260628, build
# ################################

from typing import Any
from fasthtml.common import Div, Input
from ..utils import merge_classes
from ._picker import picker_select
from .types import Color, Size, SelectVariant


def MyTime(name: str = "time", hour: int = 0, minute: int = 0, second: int = 0, 
        color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", 
        hour_kw: dict[str, Any] | None = None, minute_kw: dict[str, Any] | None = None, second_kw: dict[str, Any] | None = None, **kw):
    """Custom my-time-picker component."""
    user_cls = kw.pop("cls", None)
    hour_kw, minute_kw, second_kw = hour_kw or {}, minute_kw or {}, second_kw or {}
    hour_kw = dict(hour_kw, id=f"{name}_hour", data_time_part="hour", onchange="psiUpdateTimePicker(this)")
    minute_kw = dict(minute_kw, id=f"{name}_minute", data_time_part="minute", onchange="psiUpdateTimePicker(this)")
    second_kw = dict(second_kw, id=f"{name}_second", data_time_part="second", onchange="psiUpdateTimePicker(this)")
    return Div(
        picker_select("Hour", f"{name}_hour", range(24), hour, 2, color=color, size=size, variant=variant, select_kw=hour_kw),
        picker_select("Minute", f"{name}_minute", range(60), minute, 2, color=color, size=size, variant=variant, select_kw=minute_kw),
        picker_select("Second", f"{name}_second", range(60), second, 2, color=color, size=size, variant=variant, select_kw=second_kw),
        Input(type="hidden", name=name, value=f"{hour:02d}:{minute:02d}:{second:02d}", data_time_output=True),
        data_time_picker=name,
        cls=merge_classes("flex gap-3", user_cls),
        **kw)
