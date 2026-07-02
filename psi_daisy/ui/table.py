# ################################
# File:     table.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Table component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Table as FHTable, Thead, Tbody, Tr, Th, Td
from ..utils import merge_classes, size_cls
from .types import Size

def Table(headers: list, rows: list[list], *, size: Size = "md", zebra: bool = False,
          pin_rows: bool = False, **kw):
    """DaisyUI table component."""
    sz = size_cls("table", size)
    parts = ["table"]
    if zebra:    parts.append("table-zebra")
    if pin_rows: parts.append("table-pin-rows")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    head = Thead(Tr(*[Th(h) for h in headers]))
    body = Tbody(*[Tr(*[Td(cell) for cell in row]) for row in rows])
    return FHTable(head, body, cls=merge_classes(" ".join(parts), user_cls), **kw)
