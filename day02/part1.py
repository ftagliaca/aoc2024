from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_data(s: str) -> list[list[int]]:
    return [[int(x) for x in r.split()] for r in s.split('\n') if r]

def compute(s: str) -> int:
    reports = parse_data(s)

    s = 0
    for report in reports:
        diffs = [x1-x0 for x0,x1 in zip(report[:-1], report[1:])]
        if (report[-1] - report[0]) < 0:
            s += all([-3<=i<=-1 for i in diffs])
        else:
            s += all([1<=i<=3 for i in diffs])



    return s


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2


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
