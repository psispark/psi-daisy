# ################################
# File:     ui_classes.py
# Module:   daisy
# Author:   lucien@psispark.com
# Task:     Utility helpers for UI classes.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

def merge_classes(*classes: str | None) -> str:
    """Merge Tailwind class strings, ignoring None values."""
    return " ".join(c for c in classes if c)


def size_cls(prefix: str, size: str) -> str:
    """Return DaisyUI size class for a given prefix and size, empty string for md."""
    return "" if size == "md" else f"{prefix}-{size}"
