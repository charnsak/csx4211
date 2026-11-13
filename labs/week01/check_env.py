"""Week 1 - check that your codespace has the tools this course needs.

Run from the repository root:
    python labs/week01/check_env.py
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys

results: list[bool] = []


def report(name: str, ok: bool, detail: str, hint: str = "") -> None:
    """Print one PASS/FAIL line and remember the result."""
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name:<8} {detail}")
    if not ok and hint:
        print(f"         hint: {hint}")


def first_line(cmd: list[str]) -> tuple[bool, str]:
    """Run a command; return (succeeded, first line of its output)."""
    if shutil.which(cmd[0]) is None:
        return False, f"'{cmd[0]}' is not installed"
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, "timed out"
    text = proc.stdout.strip() or proc.stderr.strip()
    # Skip JVM notices such as "Picked up JAVA_TOOL_OPTIONS: ..." and keep the first real line.
    lines = [line for line in text.splitlines() if line.strip() and not line.startswith("Picked up")]
    return proc.returncode == 0, lines[0][:100] if lines else ""


def main() -> int:
    print("CSX4211 environment check\n")

    report("python", sys.version_info >= (3, 11), platform.python_version(),
           "Open the course codespace; it has Python 3.12.")

    ok, out = first_line(["git", "--version"])
    report("git", ok, out)

    ok, out = first_line(["docker", "version", "--format", "{{.Server.Version}}"])
    report("docker", ok, f"engine {out}" if ok else out,
           "Docker starts in the background. Wait one minute, then run this script again.")

    ok, out = first_line(["java", "-version"])
    report("java", ok, out,
           "Needed from Week 5. Command Palette (Ctrl+Shift+P) > 'Codespaces: Rebuild Container'.")

    try:
        import duckdb
        report("duckdb", True, duckdb.__version__)
    except ImportError:
        report("duckdb", False, "not installed",
               "Run: pip3 install --user -r requirements.txt")

    cores = os.cpu_count() or 0
    ram_gb = 0.0
    if hasattr(os, "sysconf"):
        ram_gb = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 1024**3
    free_gb = shutil.disk_usage(os.getcwd()).free / 1024**3
    in_codespace = os.environ.get("CODESPACES") == "true"
    print(f"\nMachine: {cores} cores, {ram_gb:.0f} GB RAM, {free_gb:.0f} GB free disk")
    print(f"Running in GitHub Codespaces: {'yes' if in_codespace else 'no'}")

    if all(results):
        print("\nAll checks passed. You are ready for the Week 1 lab.")
        return 0
    print(f"\n{results.count(False)} check(s) failed. Read the hints above, or ask a lab captain.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
