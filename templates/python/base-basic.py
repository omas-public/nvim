from bisect import bisect
from sys import stdin

# utility function
identity = I = lambda x: x
consistent = K = lambda x: lambda y: x
bisect_pick = lambda d, value: list(d.values())[bisect(list(d.keys()), value) - 1]
join = lambda sep="\n", fn=str: lambda values: sep.join(map(fn, values))
split = lambda sep=" ", fn=I: lambda v: list(map(fn, v.split(sep)))

# 入力を受け取りリストにして返す関数
def gets(n, fn=I):
    return [fn(line) for line in stdin.read().split('\n')[:n]]

#　出力関数
def puts(value, fn=str):
    print(fn(value))

# 入力データを受取り加工して返す関数
def main(p):
    buff = p
    return buff

# 出力用に加工する関数
def transform(p):
    buff = p
    return buff


if __name__ == "__main__":

    # preprocessing
    _in = gets(1)[0]

    # main function
    _out = main(_in)

    # display
    puts(transform(_out))
