from bisect import bisect
from sys import stdin

identity = I = lambda x: x
consistent = K = lambda x: y: x
join = lambda sep="\n", fn=str: lambda values: sep.join(map(fn, values))
split = lambda sep=" ", fn=I: lambda v: list(map(fn, v.split(sep)))


def bisect_pick(dic, value):
    return list(dic.values())[bisect(list(dic.keys()), value) - 1]


def gets(n, fn=I):
    return [fn(line) for line in stdin.read().split('\n')[:n]]


def puts(value, fn=str):
    print(fn(value))


def main(p):
    buff = p
    return buff


def transform(p):
    buff = p
    return buff


if __name__ == "__main__":

    # preprocessing
    _stdin = gets(1)

    # main function
    _stdout = main(_stdin)

    # display
    puts(_stdout)
