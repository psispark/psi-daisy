# ################################
# File:     widgets.py
# Module:   examples.utils
# Author:   lucien@psispark.com
# Task:     Shared UI widgets for psi-daisy demos.
# Release:  v0.1
# History:
#   * 001, ai, 260607, refactor
#   * 002, Luch, 260608, fixed package path 
#   * 003, Luch, 260608, added theme select  
# ################################

from fasthtml.common import *
from fasthtml.common import Select as TallSelect
from psi_daisy.ui import Toggle, Select, Label, Checkbox 
from examples.utils.introspect import all_components, get_component_fn, get_param_info
from examples.utils.js import js_exclusive_all


def mk_theme_toggle():
    return Label(
        Span("☀️", cls="text-lg"),
        Toggle(
            cls="theme-controller toggle mx-1",
            value="dark",
            hx_on="change: document.documentElement.setAttribute('data-theme', this.checked ? 'dark' : 'light')"),
        Span("🌙", cls="text-lg"),
        cls="flex items-center gap-1 cursor-pointer ml-4"
    )


def mk_comp_select(comp="button"):
    comps = all_components()
    return Select(
        *[Option(c.replace('_', ' ').title(), value=c, selected=(c == comp)) for c in comps],
        name="component", id="comp-sel",
        hx_post="/update-args", hx_target="#args-panel", hx_trigger="change",
        hx_on__htmx_before_request="document.getElementById('display').innerHTML=''",
        cls="w-full max-w-xs",
    )


def mk_args_panel(component="button"):
    # TODO: fix All + other items multi-select (ties in with JS oninput handler)
    fn = get_component_fn(component)
    if fn is None:
        return Div(P("No component found."), id="args-panel")
    _, literal_params, bool_params, _ = get_param_info(fn)

    controls = []
    for pname, vals in literal_params.items():
        opts = [Option("All", value="__all__")] + [Option(v or "(default)", value=v) for v in vals]
        n = len(vals)
        large = n > 30
        if large: sel = TallSelect(*opts, name=pname, multiple=True, size=min(n+1, 24), cls="w-full border border-base-300 rounded-lg p-2 bg-base-100 text-base-content", style="min-width:28rem;height:32rem;", oninput=js_exclusive_all())  
        else: sel = Select(*opts, name=pname, multiple=True, size=min(n+1, 7), cls="w-full", oninput=js_exclusive_all())
        controls.append(Div(
            Label(pname.title(), cls="text-sm font-semibold mb-1 block text-gray-700 dark:text-gray-300"),
            sel,
            cls="flex flex-col w-full max-w-3xl" if large else "flex flex-col min-w-[150px]"))
    for pname in bool_params:
        controls.append(Div(
            Label(
                Checkbox(name=pname, value="true"),
                Span(pname.title(), cls="text-sm font-semibold text-gray-700 dark:text-gray-300"),
                cls="flex items-center gap-2 cursor-pointer"),
            cls="flex flex-col justify-end"
        ))

    inner = Div(*controls, cls="flex flex-wrap gap-6 p-4") if controls         else P("No configurable args.", cls="text-sm text-gray-400 italic")
    return Div(inner, id="args-panel", cls="flex flex-col")
    

def mk_theme_select(current="light"):
    from psi_daisy.themes import BUILTIN_THEMES, registered_themes
    reg = registered_themes()
    return Select(
        *[Option(t.title(), value=t, selected=(t == current)) for t in BUILTIN_THEMES],
        *[Option(t, value=t, selected=(t == current)) for t in reg],
        name="theme", id="theme-sel",
        onchange="applyPageTheme(this.value)",
        cls="w-full max-w-xs")
