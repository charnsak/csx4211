"""Week 1 - ask your own questions about the data with SQL.

Run hello_pipeline.py first. Then, from the repository root, either pass one query:
    python labs/week01/query.py "SELECT * FROM taxi_zones LIMIT 5"
or start an interactive prompt (type a query and press Enter; an empty line quits):
    python labs/week01/query.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import duckdb

DB_FILE = Path(__file__).resolve().parent / "data" / "week01.duckdb"


def run(con: duckdb.DuckDBPyConnection, sql: str) -> None:
    """Run one SQL statement and print its result as a table."""
    try:
        result = con.sql(sql)
    except duckdb.Error as err:
        print(f"SQL error: {err}")
        return
    if result is not None:
        result.show(max_rows=300)


def main() -> int:
    if not DB_FILE.exists():
        print("No database yet. Run this first:  python labs/week01/hello_pipeline.py")
        return 1
    with duckdb.connect(str(DB_FILE), read_only=True) as con:
        if len(sys.argv) > 1:
            run(con, " ".join(sys.argv[1:]))
            return 0
        tables = ", ".join(row[0] for row in con.execute("SHOW TABLES").fetchall())
        print(f"Tables: {tables}")
        print("Type a SQL query and press Enter. Press Enter on an empty line to quit.")
        while True:
            try:
                sql = input("sql> ").strip()
            except EOFError:
                break
            if not sql:
                break
            run(con, sql)
    return 0


if __name__ == "__main__":
    sys.exit(main())
