"""Week 1 - Hello, pipeline!

A tiny end-to-end pipeline that walks through the data engineering lifecycle:

  generation      NYC Taxi & Limousine Commission (TLC) publishes a lookup table of taxi zones
  ingestion       extract()    download the CSV file
  storage         load()       copy it into a table in a DuckDB database file
  transformation  transform()  count the zones in each borough with SQL
  serving         serve()      write a small CSV report that other people and tools can use

Run from the repository root:
    python labs/week01/hello_pipeline.py
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

import duckdb

SOURCE_URL = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
DATA = HERE / "data"
RAW_FILE = DATA / "raw" / "taxi_zone_lookup.csv"
BACKUP_FILE = DATA / "backup" / "taxi_zone_lookup.csv"  # used only if the download fails
DB_FILE = DATA / "week01.duckdb"
REPORT_FILE = DATA / "output" / "zones_per_borough.csv"


def extract() -> Path:
    """Ingestion: download the source file into data/raw/."""
    RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(SOURCE_URL, RAW_FILE)
        print(f"[extract]   downloaded {SOURCE_URL}")
    except OSError as err:
        RAW_FILE.write_bytes(BACKUP_FILE.read_bytes())
        print(f"[extract]   download failed ({err}); using the backup copy in the repo")
    return RAW_FILE


def load(con: duckdb.DuckDBPyConnection, csv_file: Path) -> None:
    """Storage: load the raw CSV file into a database table."""
    con.execute(
        f"CREATE OR REPLACE TABLE taxi_zones AS SELECT * FROM read_csv('{csv_file.as_posix()}')"
    )
    rows = con.execute("SELECT count(*) FROM taxi_zones").fetchone()[0]
    print(f"[load]      {rows} rows loaded into table taxi_zones")


def transform(con: duckdb.DuckDBPyConnection) -> None:
    """Transformation: turn raw rows into an answer - how many zones does each borough have?"""
    con.execute(
        """
        CREATE OR REPLACE TABLE zones_per_borough AS
        SELECT Borough AS borough, count(*) AS zones
        FROM taxi_zones
        GROUP BY Borough
        ORDER BY zones DESC, borough
        """
    )
    print("[transform] built table zones_per_borough")
    con.table("zones_per_borough").show()


def serve(con: duckdb.DuckDBPyConnection) -> None:
    """Serving: publish the result as a CSV file."""
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    con.execute(f"COPY zones_per_borough TO '{REPORT_FILE.as_posix()}' (HEADER, DELIMITER ',')")
    print(f"[serve]     report written to {REPORT_FILE.relative_to(REPO).as_posix()}")


def main() -> None:
    raw_file = extract()
    with duckdb.connect(str(DB_FILE)) as con:
        load(con, raw_file)
        transform(con)
        serve(con)
    print("\nPipeline finished. Explore the data with:  python labs/week01/query.py")


if __name__ == "__main__":
    main()
