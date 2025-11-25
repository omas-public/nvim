from sys import stdin


def identity(value):
    return value


def join(sep, values, fun=str):
    return sep.join([fun(value) for value in values])


class IN:
    def __init__(self):
        self.lines = [line.rstrip() for line in stdin.readlines()]

    def readline(self, fun=identity, index=0):
        return fun(self.lines[index])

    def readlines(self, fun=identity):
        return [fun(line) for line in self.lines]

    def readcols(self, fun=identity, sep=None):
        return [fun(col) for col in self.lines[0].split(sep)]

    def readmatrix(self, fun=identity, sep=None):
        return [list(map(fun, line.split(sep))) for line in self.lines]


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
    s_in = IN()
    inputs = s_in.readlines()

    # call function
    result = processing(inputs)

    # display
    s_out = OUT(result)
    s_out.printlines()
