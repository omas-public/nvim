def in_(n):
    buff = [input() for _ in range(n)]
    return buff


def fun_(p):
    buff = p
    return buff


def out_(p):
    buff = p
    print(buff)


if __name__ == "__main__":

    # preprocessing
    stdin = in_(1)

    # main function
    stdout = fun_(stdin)

    # display
    out_(stdout)
