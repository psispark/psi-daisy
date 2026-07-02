# ################################
# File:     constants.py
# Module:   examples.utils
# Author:   lucien@psispark.com
# Task:     Shared constants for psi-daisy demos.
# Release:  v0.2
# History:
#   * 001, ai, 260607, refactor
#   * 002, luch, 260623, fix finename mismatch
# ################################

from fasthtml.common import *
from psi_daisy.ui.types import Theme

BUILTIN_THEMES = list(Theme.__args__)

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

SAMPLE_ARGS = {
    "title":       "Sample Title",
    "src":         "https://picsum.photos/64",
    "alt":         "avatar",
    "label":       "Label",
    "text":        "Sample text",
    "name":        "item",
    "href":        "#",
    "value":       "42",
}

SAMPLE_CHILDREN = {
    "accordion":    [P(LOREM)],
    "alert":        [P("This is an alert message.")],
    "card":         [H3("Card Title", cls="font-bold"), P(LOREM)],
    "carousel":     [Div("Slide 1", cls="w-full h-32 flex items-center justify-center bg-base-200"),
                      Div("Slide 2", cls="w-full h-32 flex items-center justify-center bg-base-300")],
    "chat_bubble":  [P("Hello there!"), P("How are you?")],
    "collapse":     [P(LOREM)],
    "drawer":       [P("Drawer content here.")],
    "dropdown":     [Li(A("Item 1", href="#")), Li(A("Item 2", href="#")), Li(A("Item 3", href="#"))],
    "hero":         [H1("Hero Title", cls="text-4xl font-bold"), P(LOREM)],
    "menu":         [Li(A("Home", href="#")), Li(A("About", href="#")), Li(A("Contact", href="#"))],
    "modal":        [P("Modal body content.")],
    "steps":        [Li("Step 1", cls="step step-primary"), Li("Step 2", cls="step"), Li("Step 3", cls="step")],
    "tabs":         [("Tab 1", "Content 1"), ("Tab 2", "Content 2"), ("Tab 3", "Content 3")],
    "table":        [Tr(Th("Name"), Th("Age")), Tr(Td("Alice"), Td("30")), Tr(Td("Bob"), Td("25"))],
    "timeline":     [Li(P("Event 1")), Li(P("Event 2")), Li(P("Event 3"))],
    "toast":        [P("Toast notification!")],
    "tooltip":      [],
    "_default":     [P(LOREM)],
}
