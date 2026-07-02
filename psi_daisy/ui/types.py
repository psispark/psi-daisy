# ################################
# File:     types.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     DaisyUI type definitions.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260608, added theme
#   * 003, luch, 260622, added variants
# ################################

from typing import Literal
from matplotlib.colors import CSS4_COLORS

WebColor     = Literal[*tuple(CSS4_COLORS.keys())]

Color        = Literal["primary", "secondary", "accent", "info", "success", "warning", "error"]
Size         = Literal["xs", "sm", "md", "lg"]
Orientation  = Literal["horizontal", "vertical"]
Position     = Literal["top", "bottom", "left", "right"]
FABPosition  = Literal["bottom-right", "bottom-left", "top-right", "top-left"]
SnapAlign    = Literal["start", "center", "end"]
IconStyle    = Literal["arrow", "plus"]
ChatSide     = Literal["start", "end"]
MaskShape    = Literal["squircle", "heart", "hexagon", "triangle", "circle", "diamond", "square", "parallelogram"]
ToastPos     = Literal["start", "center", "end"]
ToastVPos    = Literal["top", "middle", "bottom"]
Theme        = Literal["light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", 
                        "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", 
                        "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", 
                        "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"]

AlertVariant = Literal["", "soft", "outline", "dash"]
ButtonVariant = Literal["", "outline", "soft", "dash", "link", "ghost"]
BadgeVariant = Literal["", "outline", "soft", "dash", "ghost"]
SelectVariant = Literal["", "bordered", "ghost"]
InputVariant = Literal["", "bordered", "ghost"]
FileInputVariant = Literal["", "bordered", "ghost"]
TextareaVariant = Literal["", "bordered", "ghost"]
LoadingVariant = Literal["spinner", "dots", "ring", "ball", "bars", "infinity"]
TabsVariant = Literal["", "box", "border"]
