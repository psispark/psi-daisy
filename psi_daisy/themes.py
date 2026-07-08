import json, re, httpx, math
from fasthtml.common import Script
from psi_daisy.config import THEMES_DIR, REGISTRY, DAISYUI_THEMES_CSS_PATH
from .ui.types import Theme

BUILTIN_THEMES = list(Theme.__args__)

CSS_VARS = [
    "color-base-100", "color-base-200", "color-base-300", "color-base-content",
    "color-primary", "color-primary-content", "color-secondary", "color-secondary-content",
    "color-accent", "color-accent-content", "color-neutral", "color-neutral-content",
    "color-info", "color-info-content", "color-success", "color-success-content",
    "color-warning", "color-warning-content", "color-error", "color-error-content", ]

_APPLY_THEME_JS = r"""
function applyPageTheme(name) {
    const el = document.documentElement;
    el.setAttribute('data-theme', name);
    const vars = (typeof CUSTOM_THEME_VARS !== 'undefined') ? CUSTOM_THEME_VARS[name] : null;
    ALL_CSS_VARS.forEach(v => el.style.removeProperty('--' + v));
    if (vars) Object.entries(vars).forEach(([k,v]) => el.style.setProperty('--' + k, v));
}"""


def _fetch_builtin_vars():
    """Fetch and parse DaisyUI v5 themes.css, return {theme: {var: val}}."""
    try:
        css = httpx.get(DAISYUI_THEMES_CSS_PATH, follow_redirects=True, timeout=10).text
        themes = {}
        for m in re.finditer(r'\[data-theme=(\w+)\]\s*\{([^}]+)\}', css):
            name, body = m.group(1), m.group(2)
            themes[name] = {vm.group(1): vm.group(2).strip() for vm in re.finditer(r'--([\w-]+):\s*([^;]+);', body)}
        return themes
    except Exception: return {}


BUILTIN_VARS = _fetch_builtin_vars()


def registered_themes(): return json.loads(REGISTRY.read_text())


def load_custom_vars(theme):
    """Load vars dict from saved custom theme file."""
    path = THEMES_DIR / f"{theme}.css"
    if not path.exists(): return {}
    return {m.group(1): m.group(2).strip() for m in re.finditer(r'--([\w-]+):\s*([^;]+);', path.read_text())}


def save_theme(name, css):
    """Save theme to custom theme registry."""
    (THEMES_DIR / f"{name}.css").write_text(css)
    reg = registered_themes()
    if name not in reg: reg.append(name); REGISTRY.write_text(json.dumps(reg))


def theme_script():
    """Return Script tag with custom theme data and applyPageTheme function."""
    reg = registered_themes()
    custom_vars = {t: load_custom_vars(t) for t in reg}
    return Script(
        f"const SAVED_THEMES = {json.dumps(reg)};\n"
        f"const CUSTOM_THEME_VARS = {json.dumps(custom_vars)};\n"
        f"const ALL_CSS_VARS = {json.dumps(CSS_VARS)};\n"
        + _APPLY_THEME_JS)


def oklch_to_hex(val):
    """Convert oklch(...) string to #rrggbb #hex string."""
    val = re.sub(r'oklch\(|\)', '', val).replace('%','').strip()
    parts = val.split()
    if len(parts) < 2: return "#888888"
    L, C, H = float(parts[0])/100, float(parts[1]), float(parts[2]) if len(parts) > 2 else 0
    h = math.radians(H)
    a, b = C*math.cos(h), C*math.sin(h)
    l_ = (L + 0.3963377774*a + 0.2158037573*b)**3
    m_ = (L - 0.1055613458*a - 0.0638541728*b)**3
    s_ = (L - 0.0894841775*a - 1.2914855480*b)**3
    r  =  4.0767416621*l_ - 3.3077115913*m_ + 0.2309699292*s_
    g  = -1.2684380046*l_ + 2.6097574011*m_ - 0.3413193965*s_
    b2 = -0.0041960863*l_ - 0.7034186147*m_ + 1.7076147010*s_
    def lin(v): return 12.92*v if v <= 0.0031308 else 1.055*v**(1/2.4) - 0.055
    r, g, b2 = [max(0, min(1, lin(x))) for x in (r, g, b2)]
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b2*255):02x}"


def hex_to_oklch(hex_color):
    """Convert #rrggbb #hex to oklch(...) string."""
    h = hex_color.lstrip('#')
    r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    def unlin(v): return v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4
    r, g, b = unlin(r), unlin(g), unlin(b)
    l_ = (0.4122214708*r + 0.5363325363*g + 0.0514459929*b)**(1/3)
    m_ = (0.2119034982*r + 0.6806995451*g + 0.1073969566*b)**(1/3)
    s_ = (0.0883024619*r + 0.2817188376*g + 0.6299787005*b)**(1/3)
    L  =  0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_
    a  =  1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_
    bv =  0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_
    C = math.sqrt(a**2 + bv**2)
    H = math.degrees(math.atan2(bv, a)) % 360
    return f"oklch({round(L*100,1)}% {round(C,4)} {round(H,1)})"


def hex_to_rgb(hex_color):
    """Convert #rrggbb #hex to rgb(...) string."""
    h = hex_color.lstrip('#')
    return f"rgb({int(h[0:2],16)}, {int(h[2:4],16)}, {int(h[4:6],16)})"


def vals_to_css(vals, selector='custom-preview'):
    """Generate a CSS block from a dictionary of theme color values."""
    lines = "\n".join(f"    --{v}: {vals.get(v, 'oklch(50% 0 0)')};" for v in CSS_VARS)
    return f"[data-theme='{selector}'] {{\n{lines}\n}}"


def form_to_css(form, selector='custom-preview'):
    """Convert form hex values to OKLCH and generate a preview CSS block."""
    lines = "\n".join(f"    --{v}: {hex_to_oklch(form.get('var_' + v.replace('-','_'), '#888888'))};" for v in CSS_VARS)
    return f"[data-theme='{selector}'] {{\n{lines}\n}}"


def form_to_save_css(form, name):
    """Convert form hex values to OKLCH and generate a named CSS block to save."""
    lines = "\n".join(f"    --{v}: {hex_to_oklch(form.get('var_' + v.replace('-','_'), '#888888'))};" for v in CSS_VARS)
    return f"[data-theme='{name}'] {{\n{lines}\n}}"


def parse_css_vars(css_text):
    """Extract custom CSS properties from string into dictionary."""
    return {m.group(1): m.group(2).strip() for m in re.finditer(r'--([\w-]+):\s*([^;]+);', css_text)}
