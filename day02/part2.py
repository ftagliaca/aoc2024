from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_data(s: str) -> list[list[int]]:
    return [[int(x) for x in r.split()] for r in s.split('\n') if r]

def c(l: list[int]) -> tuple[bool, int | None]:
    dic = (l[-1] - l[0]) < 0
    for i, k in enumerate(l[:-1]):
        d = l[i+1] - k
        if dic and not (-3<=d<=-1):
            return False
        if not dic and not (1<=d<=3):
            return False
    return True

def compute(s: str) -> int:
    reports = parse_data(s)

    v = 0
    for report in reports:
        for i in range(len(report)):
            r1 = report[:i]+report[i+1:]
            if c(r1):
                v += 1
                break

    return v

INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 4


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
