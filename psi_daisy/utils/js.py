# ################################
# File:     js.py
# Module:   utils
# Author:   lucien@psispark.com
# Task:     JS helpers for psi-daisy demos.
# Release:  v0.1
# History:
#   * 001, Luch, 260607, build
#   * version, who, when, why
# ################################


def js_exclusive_all(all_value="__all__"):
    """Select either 'All' or specific items, never both."""
    return f"""
        const all = this.querySelector('[value="{all_value}"]');
        const others = [...this.options].filter(o => o.value !== '{all_value}');
        if (all.selected) {{
            others.forEach(o => o.selected = false);
        }} else {{
            if ([...others].some(o => o.selected)) all.selected = false;
        }} """
