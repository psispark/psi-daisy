# ################################
# File:     db.py
# Module:   examples.utils
# Author:   lucien@psispark.com
# Task:     Shared db helpers for psi-daisy demos.
# Release:  v0.2
# History:
#   * 001, Luch, 260629, build
# ################################

import sqlite3
from pathlib import Path
from psi_daisy.config import ICONS_DB

db_path = ICONS_DB


def mk_conx(path:Path=db_path) -> sqlite3.Connection:
    """Get connection to sqlite db in path."""
    conx = sqlite3.connect(path)
    conx.row_factory = sqlite3.Row
    return conx


def query(conx:sqlite3.Connection, sql:str, params:tuple=()) -> list[sqlite3.Row]: return conx.execute(sql, params).fetchall()
