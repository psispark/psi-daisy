# ################################
# File:     my_color.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Build a color picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260630, build
# ################################

import re,json
from matplotlib.colors import CSS4_COLORS
from fasthtml.common import Div, Span, Code, Li, A
from . import Input, Label, Button, Select, Dropdown
from ..themes import hex_to_rgb, hex_to_oklch
from .types import WebColor
from ..utils import merge_classes

colors = json.dumps([[k,v.lower()] for k,v in CSS4_COLORS.items()])
items = [Li(A(k, cls="whitespace-nowrap", onclick=f"let i=this.closest('[data-color-picker]').querySelector('input[type=color]');i.value='{v.lower()}';psiUpdateColorPicker(i)"), cls="w-full") for k,v in CSS4_COLORS.items()]

pick_js = """psiUpdateColorPicker(this);
    let r=this.closest('[data-color-picker]'),
        s=r.querySelector('select'),
        w=r.querySelector('[data-color-name]');
    if(s) {
    s.classList.add('hidden');
    s.selectedIndex=-1; }
    if(w) w.textContent='web: '""".strip()

web_js = f"""
    let d=this.closest('.dropdown'),
        m=d.querySelector('ul'),
        r=this.closest('[data-color-picker]'),
        i=r.querySelector('input[type=color]'),
        w=r.querySelector('[data-color-name]');
    if(!m.children.length) {{
    {colors}.forEach(o => {{
        let li=document.createElement('li'),
            a=document.createElement('a');
        li.className='w-full';
        a.textContent=o[0];
        a.dataset.val=o[1];
        a.className='whitespace-nowrap';
        a.onclick=() => {{
        i.value=o[1];
        psiUpdateColorPicker(i);
        if(w) w.textContent='web: '+o[0];
        [...m.querySelectorAll('a')].forEach(x => x.classList.remove('active'));
        a.classList.add('active'); }};
        li.appendChild(a);
        m.appendChild(li); }}); }}
    [...m.querySelectorAll('a')].forEach(a => a.classList.toggle('active', a.dataset.val==i.value))""".strip()


def valid_hex(o:str|None) -> bool: return bool(o and re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", o))


def color_name(hex_color:str) -> str:
    """CSS4 color name for given hex code if found."""
    hits = [k for k,v in CSS4_COLORS.items() if v.lower()==hex_color.lower()]
    return hits[0] if hits else ""


def MyColor(name:str="color", web_color:WebColor="dodgerblue", hex_color:str|None=None, label:str|None="Color", show_outputs:bool=False, input_kw:dict|None=None, **kw):
    """Custom color picker component with color codes"""
    user_cls = kw.pop("cls", None)
    input_kw = input_kw or {}
    hex_val = hex_color.lower() if valid_hex(hex_color) else CSS4_COLORS.get(web_color, CSS4_COLORS["dodgerblue"]).lower()
    nm, rgb, oklch = color_name(hex_val), hex_to_rgb(hex_val), hex_to_oklch(hex_val)
    outs = Div(
        Code(f"web: {nm}", cls="text-xs text-base-content/60", data_color_name=True),
        Code(f"rgb: {rgb}", cls="text-xs text-base-content/60", data_color_rgb=True),
        Code(f"hex: {hex_val}", cls="text-xs text-base-content/60", data_color_hex=True),
        Code(f"oklch: {oklch}", cls="text-xs text-base-content/60", data_color_oklch=True),
        cls="flex flex-col gap-1")
    inp = Input(type="color", name=name, value=hex_val, cls="w-14 h-10 cursor-pointer rounded border-0 p-0", oninput=pick_js, onchange=pick_js, **input_kw)
    web = Dropdown(Button("colors▾", color='primary', size='xs', variant='ghost', cls="whitespace-nowrap -mt-2", onclick=web_js), menu_cls="w-36 max-h-32 overflow-y-auto overflow-x-hidden")
    ctrls = Div(inp, web, cls="flex flex-col items-start gap-0")    
    body = Div(ctrls, outs, cls="flex items-start gap-5") if show_outputs else Div(ctrls, cls="flex items-start gap-3")
    return Div(Label(Span(label), cls="label") if label else None, body, data_color_picker=True, cls=merge_classes("flex flex-col gap-1", user_cls), **kw)
