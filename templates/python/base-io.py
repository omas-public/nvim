from sys import stdin

identity = lambda  value: value
join = lambda sep,values,fun = str: sep.join([fun(value) for value in values])
class IN:
    def __init__(self):
        self.lines = [line.rstrip() for line in stdin.readlines()]
    readline = lambda self, fun = identity, index = 0: fun(self.lines[index])
    readlines = lambda self, fun = identity: [fun(line) for line in self.lines]
    readcols = lambda self, fun = identity, sep = None: [fun(col) for col in self.lines[0].split(sep)]
    readmatrix = lambda self, fun = identity, sep = None:[list(map(fun, line.split(sep))) for line in self.lines]

class OUT:
    def __init__(self, values):
        self.values = values
    printline = lambda self: print(self.values)
    printlines = lambda self: print(join('\n', self.values))
    printcols = lambda self: print(join(' ', self.values))
    printmatrix = lambda self: print(join('\n',[join(' ', cols) for cols in self.values]))

# edit below

def processing(values):
    return values

if __name__=="__main__":
    # preprocessing
    stdin = IN()
    inputs = stdin.readlines()


    # call function
    result = processing(inputs)


    # display
    stdout = OUT(result)
    stdout.printlines()
