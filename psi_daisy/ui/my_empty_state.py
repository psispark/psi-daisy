# ################################
# File:     my_empty_state.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Empty State component.
# Release:  v0.2
# History:
#   * 001, luch, 260624, build
# ################################

from typing import Literal
from fasthtml.common import Div, H2, P
from ..utils import merge_classes
from . import Hero, Card 
from .types import Color

EmptyStateVariant = Literal["hero", "card"]


def MyEmptyState(
    title: str,
    *,
    body: str = "",
    icon=None,
    action=None,
    color: Color | None = None,
    variant: EmptyStateVariant = "hero",
    compact: bool = True,
    **kw,
):
    """Custom my-empty-state component."""
    user_cls = kw.pop("cls", None)
    tone_cls = f"text-{color}" if color else "text-base-content"

    children = []
    if icon: children.append(Div(icon, cls=merge_classes("text-5xl mb-4", tone_cls)))
    children.append(H2(title, cls="text-2xl font-bold"))
    if body: children.append(P(body, cls="text-base-content/60"))
    if action: children.append(Div(action, cls="mt-4"))

    content = Div(*children, cls="max-w-md space-y-3 text-center")
    base_cls = merge_classes("my-empty-state", user_cls)

    if variant == "card": return Card(content, cls=base_cls, **kw)

    hero_cls = "min-h-48" if compact else "min-h-80"
    return Hero(content, cls=merge_classes(base_cls, hero_cls), **kw)
