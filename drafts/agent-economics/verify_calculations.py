"""Audit the arithmetic printed in post.md using only the Python standard library.

Prices are the dated snapshot in claims-and-calculations.md. This checks arithmetic
and draft consistency, not live prices, measured model quality, or prose semantics.
"""
from decimal import Decimal as D
from pathlib import Path


ROOT = Path(__file__).resolve().parent
# USD per million: fresh input, cache read, cache write, output.
RATES = {
    "Opus 5 → Sonnet 5": (
        tuple(map(D, ("5", ".5", "6.25", "25"))),
        tuple(map(D, ("2", ".2", "2.5", "10"))),
    ),
    "GPT-5.6 Sol → Terra": (
        tuple(map(D, ("4", ".4", "5", "20"))),
        tuple(map(D, ("2", ".2", "2.5", "12"))),
    ),
}


def money_range(low, high):
    return f"${low:.2f}" if low == high else f"${low:.2f}–${high:.2f}"


def seconds_range(low, high):
    return f"{low:.0f} seconds" if low == high else f"{low:.0f}–{high:.0f} seconds"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit(post):
    rows = [tuple(cell.strip() for cell in line.strip("|").split("|"))
            for line in post.splitlines() if line.startswith("| ")]
    checks = 0

    def passed(label):
        nonlocal checks
        checks += 1
        print(f"PASS {label}")

    cost_rows = [row for row in rows if row[0] in RATES]
    require(len(cost_rows) == 4, "Expected four pricing comparisons")
    require({(row[0], row[1]) for row in cost_rows}
            == {(name, use) for name in RATES for use in ("Same", "1.5×")},
            "Missing or duplicate pricing scenario")
    for name, use, saving, attention in cost_rows:
        high, mid = RATES[name]
        multiplier = D(1) if use == "Same" else D(use.rstrip("×"))
        ratios = [m / h for h, m in zip(high, mid)]
        low = D(5) * (1 - max(ratios) * multiplier)
        high = D(5) * (1 - min(ratios) * multiplier)
        require(saving == money_range(low, high), f"Incorrect saving: {name}, {use}")
        require(attention == seconds_range(low * 36, high * 36),
                f"Incorrect attention allowance: {name}, {use}")
        passed(f"pricing row: {name}, {use}")

    require(f"{D(3) * 60 / 100:.1f} minutes" in post, "Missing opening allowance")
    require(f"${D(2) * 100 / 60:.2f} to save $3" in post, "Incorrect two-minute cost")
    for name, (high, mid) in RATES.items():
        doubled = [D(5) * (1 - 2 * m / h) for h, m in zip(high, mid)]
        if name.startswith("Opus"):
            require(min(doubled) == max(doubled) == D(1), "Sonnet doubling changed")
            require("shrinks to $1" in post, "Missing doubled-token Sonnet example")
        else:
            require(min(doubled) == -1 and max(doubled) == 0, "Terra doubling changed")
            require("breaks even or costs up to $1 more" in post, "Missing Terra doubling example")
    passed("attention conversion and doubled-token examples")

    require("published: false" in post, "Draft publication flag changed")
    require("\u2014" not in post, "Em dash found")
    require("/Users/" not in post, "Local filesystem path in public-facing copy")
    passed("draft publication and hygiene markers")
    return checks


if __name__ == "__main__":
    count = audit((ROOT / "post.md").read_text(encoding="utf-8"))
    print(f"{count} named checks passed; no API calls or files written.")
