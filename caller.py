import inspect

def red( x):
    return "\033[31m{}\033[m".format(x)

def green( x):
    return "\033[32m{}\033[m".format(x)

def yellow( x):
    return "\033[33m{}\033[m".format(x)

def blue( x):
    return "\033[34m{}\033[m".format(x)


class Caller:
    def emit(self, msg):
        file = inspect.stack()[1][1]
        line = inspect.stack()[1][2]
        func = inspect.stack()[1][3]
        print("{}   {} {} {} {} ".format(msg, blue("|"), yellow(file), yellow(line), func )  )

    # def verdict(self, isOk, msg):
    #     file = inspect.stack()[1][1]
    #     line = inspect.stack()[1][2]
    #     func = inspect.stack()[1][3]
    #     if isOk == True:
    #         print("{} {} {} {}".format(green("PASS"), msg, blue("|"), func )  )
    #     else:
    #         print("{} {} {} {}".format(red("FAIL"), msg, blue("|"), func )  )

    def verdict(self, expected, actual):
        file = inspect.stack()[1][1]
        line = inspect.stack()[1][2]
        func = inspect.stack()[1][3]

        if expected == actual:
            print("{} | {} | {}".format(green("PASS"), line, func )  )
        else:
            print("{} | {} | {}".format(red("FAIL"), line, func )  )

