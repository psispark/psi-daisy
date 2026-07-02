# ################################
# File:     _picker.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Shared helpers for picker-style components.
# Release:  v0.2
# History:
#   * 001, luch, 260628, build
# ################################

from typing import Iterable, Any
import json
from matplotlib.colors import CSS4_COLORS
from fasthtml.common import Div, Option, Span, Script
from . import Select, Label
from .types import Color, Size, SelectVariant

color_names_js = {v.lower():k for k,v in CSS4_COLORS.items()}


def _label_cls(size: Size) -> str: return dict(xs="text-xs", sm="text-sm", md="text-base", lg="text-lg").get(size, "text-base")


def picker_select(label: str, name: str, values: Iterable[int], selected: int, pad: int = 0, 
        color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", select_kw: dict[str, Any] | None = None):
    """common option picker logic using a select component"""
    select_kw = select_kw or {}
    opts = [Option(str(v).zfill(pad), value=str(v), selected=(v == selected)) for v in values]
    return Div(
        Label(Span(label, cls=_label_cls(size)), cls="label"), 
        Select(*opts, name=name, color=color, size=size, variant=variant, **select_kw), cls="flex flex-col gap-1") 


def get_date_picker_headers() -> list[Any]:
    """js to dynamically limit days to month and leap year"""
    return [Script("""
function psiDaysInMonth(year, month) {
    return new Date(year, month, 0).getDate();
}
function psiUpdateDatePicker(el) {
    const root = el.closest("[data-date-picker]");
    const name = root.dataset.datePicker;
    const y = root.querySelector(`[name="${name}_year"]`);
    const m = root.querySelector(`[name="${name}_month"]`);
    const d = root.querySelector(`[name="${name}_day"]`);
    const cur = parseInt(d.value || "1");
    const maxDay = psiDaysInMonth(parseInt(y.value), parseInt(m.value));
    d.innerHTML = "";
    for (let i=1; i<=maxDay; i++) {
        const opt = document.createElement("option");
        opt.value = String(i);
        opt.textContent = String(i).padStart(2, "0");
        if (i === Math.min(cur, maxDay)) opt.selected = true;
        d.appendChild(opt);
    }
}
""")]    


def get_color_picker_headers() -> list[Any]:
    "js to update color picker outputs"
    return [Script(f"""
window.psiColorNames = window.psiColorNames || {json.dumps(color_names_js)};
function psiHexToRgb(hex) {{
    hex = hex.replace('#','');
    if (hex.length === 3) hex = hex.split('').map(x => x+x).join('');
    const n = parseInt(hex, 16);
    return `rgb(${{(n>>16)&255}}, ${{(n>>8)&255}}, ${{n&255}})`;
}}
function psiRgbToOklch(hex) {{
    hex = hex.replace('#','');
    if (hex.length === 3) hex = hex.split('').map(x => x+x).join('');
    let r = ((parseInt(hex.slice(0,2),16)/255) <= 0.04045) ? parseInt(hex.slice(0,2),16)/255/12.92 : Math.pow((parseInt(hex.slice(0,2),16)/255+0.055)/1.055, 2.4);
    let g = ((parseInt(hex.slice(2,4),16)/255) <= 0.04045) ? parseInt(hex.slice(2,4),16)/255/12.92 : Math.pow((parseInt(hex.slice(2,4),16)/255+0.055)/1.055, 2.4);
    let b = ((parseInt(hex.slice(4,6),16)/255) <= 0.04045) ? parseInt(hex.slice(4,6),16)/255/12.92 : Math.pow((parseInt(hex.slice(4,6),16)/255+0.055)/1.055, 2.4);
    let l = Math.cbrt(0.4122214708*r + 0.5363325363*g + 0.0514459929*b);
    let m = Math.cbrt(0.2119034982*r + 0.6806995451*g + 0.1073969566*b);
    let s = Math.cbrt(0.0883024619*r + 0.2817188376*g + 0.6299787005*b);
    let L = 0.2104542553*l + 0.7936177850*m - 0.0040720468*s;
    let a = 1.9779984951*l - 2.4285922050*m + 0.4505937099*s;
    let c = 0.0259040371*l + 0.7827717662*m - 0.8086757660*s;
    let C = Math.sqrt(a*a + c*c);
    let H = (Math.atan2(c, a) * 180 / Math.PI + 360) % 360;
    return `oklch(${{(L*100).toFixed(3)}}% ${{C.toFixed(3)}} ${{H.toFixed(3)}})`;
}}
function psiUpdateColorPicker(el) {{
    const root = el.closest('[data-color-picker]');
    const hex = el.value.toLowerCase();
    const nameEl = root.querySelector('[data-color-name]');
    const hexEl = root.querySelector('[data-color-hex]');
    const rgbEl = root.querySelector('[data-color-rgb]');
    const oklchEl = root.querySelector('[data-color-oklch]');
    if (nameEl) nameEl.textContent = `name: ${{window.psiColorNames[hex] || ""}}`;
    if (hexEl) hexEl.textContent = `hex: ${{hex}}`;
    if (rgbEl) rgbEl.textContent = `rgb: ${{psiHexToRgb(hex)}}`;
    if (oklchEl) oklchEl.textContent = `oklch: ${{psiRgbToOklch(hex)}}`;
}}
""")]
