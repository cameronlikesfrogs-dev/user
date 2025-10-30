
from __future__ import annotations
import sys
import math

def mean_of_three(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3.0

def parse_arg_as_number(s: str) -> float:
    try:
        val = float(s)
    except ValueError:
        raise ValueError(f"Not a valid number: {s!r}")
    if not math.isfinite(val):
        raise ValueError(f"Number must be finite: {s!r}")
    return val

def get_number(prompt: str) -> float:
    while True:
        try:
            s = input(prompt).strip()
            return parse_arg_as_number(s)
        except ValueError as e:
            print(e)

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:]) if argv is None else argv
    try:
        if len(argv) == 3:
            a, b, c = (parse_arg_as_number(x) for x in argv)
        else:
            print("Enter score to tell you the average.")
            a = get_number("First score: ")
            b = get_number("Second score: ")
            c = get_number("Third score: ")
        mean = mean_of_three(a, b, c)
        # Print using full precision when needed
        print("result:", mean)
        if mean < 7:
            print("you failed")
        else:
            print("you passed")
        return 0
    except ValueError as e:
        print(e)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())