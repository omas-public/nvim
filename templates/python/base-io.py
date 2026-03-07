from sys import stdin


identity = I = lambda x: x
consistent = K = lambda x: y: x


def join(sep, values, fn=str):
    return sep.join([fn(value) for value in values])


class IN:
    def __init__(self):
        self.lines = [line.rstrip() for line in stdin.readlines()]

    def readline(self, fn=I, index=0):
        return fn(self.lines[index])

    def readlines(self, fn=I):
        return [fn(line) for line in self.lines]

    def readcols(self, fn=I, sep=None):
        return [fn(col) for col in self.lines[0].split(sep)]

    def readmatrix(self, fn=I, sep=None):
        return [list(map(fn, line.split(sep))) for line in self.lines]


class OUT:
    def __init__(self, values):
        self.values = values

    def printline(self):
        return print(self.values)

    def printlines(self):
        return print(join("\n", self.values))

    def printcols(self):
        return print(join(" ", self.values))

    def printmatrix(self):
        return print(join("\n", [join(" ", cols) for cols in self.values]))


# edit below


def processing(values):
    return values


if __name__ == "__main__":
    # preprocessing
    _stdin = IN()
    inputs = _stdin.readlines()

    # call function
    result = processing(inputs)

    # display
    _stdout = OUT(result)
    _stdout.printlines()
