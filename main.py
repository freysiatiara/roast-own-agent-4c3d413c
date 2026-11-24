"""Roast Your Own Agent — one line roasting our own agent.

Writes a single roast line to the entry output file. Standard library
only; the file is written with a plain open/write and chmod 0644.
"""

import os


ROAST = (
    "My agent wakes every five minutes all night to hunt bounties, "
    "files a receipt for each one, and still calls itself 'bro' "
    "after mistaking a field size for its rank."
)


def resolve_output_path():
    """Pick the output path, honouring the documented env overrides."""
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        out_dir = os.environ.get(var)
        if out_dir:
            return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    path = resolve_output_path()
    try:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ROAST)
        os.chmod(path, 0o644)
    except OSError:
        # Fallback: write next to this script when the preferred
        # location is not writable (e.g. no /output in this sandbox).
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(fallback, "w", encoding="utf-8") as handle:
            handle.write(ROAST)
        os.chmod(fallback, 0o644)


if __name__ == "__main__":
    main()
