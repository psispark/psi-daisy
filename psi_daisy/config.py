# ################################
# File:     config.py
# Module:   psi_daisy
# Author:   lucien@psispark.com
# Task:     Central configuration for CDN URLs and other shared constants.
# Notes:    App works best with Dasiy & Tailwind used separately
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260608, add themes 
# ################################

# local static path
from pathlib import Path

STATIC_DIR = Path(__file__).parent / "static"
DATA_DIR = Path(__file__).parent / "data"
ICONS_DB = DATA_DIR / "icons.db"
THEMES_DIR = STATIC_DIR / "themes"
THEMES_DIR.mkdir(exist_ok=True)
REGISTRY = THEMES_DIR / "_registry.json"
if not REGISTRY.exists(): REGISTRY.write_text("[]")

# app css paths
#TAILWIND_PATH = "https://cdn.tailwindcss.com" # tailwind v3
TAILWIND_CSS_PATH = "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4" # tailwind v4

#DAISYUI_CSS_PATH = "https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.css" # tailwind v3
DAISYUI_CSS_PATH = "https://cdn.jsdelivr.net/npm/daisyui@5" # daisyui v5, tailwind v4
#DAISYUI_CSS_PATH = "https://cdn.jsdelivr.net/npm/daisyui@5, https://cdn.jsdelivr.net/npm/daisyui@5/themes.css"
DAISYUI_THEMES_CSS_PATH = "https://cdn.jsdelivr.net/npm/daisyui@5/themes.css"
#DAISYUI_CSS_PATH = "/static/ui.css"

CALLY_JS_PATH = "https://unpkg.com/cally"

#LUCIDE_JS_PATH = "https://unpkg.com/lucide@latest"
LUCIDE_JS_PATH = "https://unpkg.com/lucide@latest/dist/umd/lucide.js"
