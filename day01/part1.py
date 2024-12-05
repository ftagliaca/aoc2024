from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_data(s: str) -> list[list[int]]:
    return [[int(x) for x in r.split()] for r in s.split('\n') if r]

def compute(s: str) -> int:
    numbers = parse_data(s)
    lists = list(zip(*numbers))

    sorted_lists = [sorted(l) for l in lists]

    d = [abs(x1 - x0) for x0,x1 in zip(*sorted_lists)]

    return sum(d)


INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 11


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
