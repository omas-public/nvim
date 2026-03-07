identity = I = lambda x: x
consistent = K = lambda x: y: x

def gets(n, fn=I):
    buff = [fn(input()) for _ in range(n)]
    return buff


def fun(p):
    buff = p
    return buff


def puts(p):
    buff = p
    print(buff)


if __name__ == "__main__":

    # preprocessing
    _stdin = gets(1)

    # main function
    _stdout = fun(_stdin)

    # display
    puts(_stdout)
