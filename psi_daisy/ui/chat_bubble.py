# ################################
# File:     chat.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI ChatBubble component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import ChatSide

def ChatBubble(message: str, *, side: ChatSide = "start", header: str = "", footer: str = "",
               avatar=None, **kw):
    """DaisyUI chat bubble component."""
    s = "chat-start" if side == "start" else "chat-end"
    user_cls = kw.pop("cls", None)
    children = []
    if avatar:  children.append(Div(avatar, cls="chat-image avatar"))
    if header:  children.append(Div(header, cls="chat-header"))
    children.append(Div(message, cls="chat-bubble"))
    if footer:  children.append(Div(footer, cls="chat-footer"))
    return Div(*children, cls=merge_classes(f"chat {s}", user_cls), **kw)
