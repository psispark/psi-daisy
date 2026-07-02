# ################################
# File:     modal.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Modal component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Dialog, Div, Form, Button
from ..utils import merge_classes

def Modal(*children, id: str, actions=None, **kw):
    """DaisyUI modal component. Use id to open via JS: document.getElementById(id).showModal()"""
    user_cls = kw.pop("cls", None)
    action_bar = Div(actions, cls="modal-action") if actions else None
    return Dialog(
        Div(*children, *([] if not action_bar else [action_bar]), cls="modal-box"),
        Form(Button("✕", cls="btn btn-sm btn-circle btn-ghost absolute right-2 top-2"),
             method="dialog", cls="modal-backdrop"),
        id=id, cls=merge_classes("modal", user_cls), **kw)
