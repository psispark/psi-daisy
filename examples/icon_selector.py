# ################################
# File:     icon_selector.py
# Module:   examples
# Author:   lucien@psispark.com
# Task:     Lucide icon selector demo.
# Release:  v0.2
# History:
#   * 001, Luch, 260608, build
#   * version, who, when, why
# ################################

import sqlite3
from pathlib import Path
from typing import get_args
from fasthtml.common import *
from psi_daisy import psi_app
from psi_daisy.ui import Button, Divider, Label, Input, Select, Checkbox, MyIcon, MyColor, get_color_picker_headers
from psi_daisy.ui.types import Color
from psi_daisy.themes import theme_script
from psi_daisy.config import ICONS_DB
from psi_daisy.utils.widgets import mk_theme_select
from psi_daisy.utils.db import mk_conx, query

db_path = ICONS_DB
colors = list(get_args(Color))
sizes = [16,20,24,32,40,48,64,96]
strokes = [1,1.5,2,2.5,3,4]
icon_weights = (5.0,3.0,1.5,1.0,1.0,1.0,0.5)
search_placeholder = "lightbulb"

app = psi_app(hdrs=get_color_picker_headers())
rt = app.route


def as_int(o:str|None, default:int) -> int:
    try: return int(o)
    except (TypeError, ValueError): return default


def as_float(o:str|None, default:float) -> float:
    try: return float(o)
    except (TypeError, ValueError): return default


def search_icons(search:str, count:int=10, weights:tuple[float,...]=icon_weights, path:Path=db_path) -> list[sqlite3.Row]:
    "Search icons_fts by one or more words, falling back from AND to OR"
    terms = [o.replace('"', '""') for o in search.split()]
    if not terms: return []
    ws = ','.join('?' for _ in weights)
    sql = f'SELECT name,pascal_name,categories,tags,aliases,use_cases,bm25(icons_fts,{ws}) score FROM icons_fts WHERE icons_fts MATCH ? ORDER BY score LIMIT ?'
    with mk_conx(path) as con:
        res = query(con, sql, (*weights, ' '.join(f'"{o}"' for o in terms), count))
        return res if res else query(con, sql, (*weights, ' OR '.join(f'"{o}"' for o in terms), count))


def mk_select(label:str, name:str, vals:list, selected) -> FT:
    return Div(Label(label, cls="label"), Select(*[Option(str(o), value=str(o), selected=str(o)==str(selected)) for o in vals], name=name, id=name, cls="w-full"), cls="flex flex-col gap-1")


def mk_input(label:str, name:str, value:str='', placeholder:str='', typ:str='text', **kw) -> FT:
    return Div(Label(label, cls="label"), Input(name=name, id=name, value=value, placeholder=placeholder, type=typ, cls="w-full", **kw), cls="flex flex-col gap-1")


def icon_card(r:sqlite3.Row, color:Color, size:int, stroke_width:float, hex_color:str|None=None, label:str|None=None) -> FT:
    name = r['name']
    args = f'icon="{name}", color="{color}", size={size}, stroke_width={stroke_width}' if not hex_color else f'icon="{name}", color="{color}", size={size}, stroke_width={stroke_width}, hex_color="{hex_color}"'
    return Div(
        Div(MyIcon(icon=name, color=color, size=size, stroke_width=stroke_width, hex_color=hex_color), cls="h-20 flex items-center justify-center"),
        P(name, cls="text-sm font-medium text-center break-all"),
        P(label, cls="text-xs text-base-content/50") if label else None,
        cls="tooltip tooltip-bottom p-4 border border-base-300 rounded-lg flex flex-col items-center gap-3 bg-base-100",
        data_tip=f"MyIcon({args})")


def render_results(rows:list[sqlite3.Row], color:Color='primary', size:int=32, stroke_width:float=2, use_hex_color:bool=False, hex_color:str|None=None) -> FT:
    if not rows: return P("No icons found.", cls="text-base-content/60")
    cards = []
    for r in rows:
        cards.append(icon_card(r, color, size, stroke_width, label=f"theme: {color}"))
        if use_hex_color and hex_color: cards.append(icon_card(r, color, size, stroke_width, hex_color=hex_color, label=f"hex: {hex_color}"))
    return Div(*cards, cls="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4")


def render_home() -> FT:
    return Div(
        Div(H1("🔎 Icon Selector", cls="text-3xl font-bold text-base-content"), cls="flex items-center mb-6"),
        Div(H2("Theme", cls="text-lg font-semibold mb-3 text-base-content"), mk_theme_select(), cls="flex flex-col mb-4"),
        Div(Divider(), H2("Options", cls="text-lg font-semibold mb-3 text-base-content"),
            Div(
                mk_select("Color", "color", colors, "primary"),
                mk_select("Size", "size", sizes, 32),
                mk_select("Stroke width", "stroke_width", strokes, 2),
                cls="grid grid-cols-1 md:grid-cols-3 gap-3 mb-4"),
            Div(
                Label(
                    Checkbox(name="use_hex_color", id="use_hex_color", value="true", cls="checkbox-primary",
                        onchange="document.getElementById('hex-color-wrap').classList.toggle('hidden', !this.checked)"),
                    Span("Use custom hex color", cls="label-text"),
                    cls="label cursor-pointer justify-start gap-3"),
                Div(MyColor(name="hex_color", web_color="dodgerblue", hex_color=None, label=None, show_outputs=True), id="hex-color-wrap", cls="hidden"),
                cls="flex flex-col md:flex-row md:items-start gap-4"),
            id="icon-options",
            cls="flex flex-col"),
        Div(Divider(), H2("Search", cls="text-lg font-semibold mb-3 text-base-content"),
            Div(
                mk_input("Words or sentence", "search", placeholder=search_placeholder),
                mk_input("Count", "count", "10", typ="number", min="1", max="50"),
                Button("Search", hx_post="/search", hx_target="#results", hx_include="#icon-options,#search,#count"),
                cls="grid grid-cols-1 md:grid-cols-[1fr_8rem_auto] gap-3 items-end"),
            cls="flex flex-col"),
        Div(Divider(), H2("Result", cls="text-lg font-semibold mb-2 text-base-content"), Div(P("Search for an icon to see results.", cls="text-base-content/60"), id="results", cls="mt-4"), cls="flex flex-col"),
        cls="p-10 max-w-6xl mx-auto bg-base-100 min-h-screen transition-colors")


@rt("/")
def get(): return theme_script(), render_home()


@rt("/search")
async def post(req):
    form = await req.form()
    count = max(1, min(as_int(form.get("count"), 10), 50))
    size = as_int(form.get("size"), 32)
    stroke_width = as_float(form.get("stroke_width"), 2)
    color = form.get("color", "primary")
    use_hex_color = bool(form.get("use_hex_color"))
    hex_color = form.get("hex_color")
    search = form.get("search") or search_placeholder
    return render_results(search_icons(search, count), color, size, stroke_width, use_hex_color, hex_color)
