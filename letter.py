from string import ascii_lowercase
import itertools

class IDService:

    def __init__(self):
        self.gen = self.iter_all_strings()

    def iter_all_strings(self):
        size = 1
        while True:
            for s in itertools.product(ascii_lowercase, repeat=size):
                yield "".join(s)
            size +=1

    # define the generator handler
    def label_gen(self):
        for s in self.gen:
            return s


if __name__ == "__main__":
    """self test"""
    id = IDService()
    letter1 = id.label_gen()
    letter2 = id.label_gen()
    letter3 = id.label_gen()
    expected = "a b c"
    actual = "{} {} {}".format(letter1, letter2, letter3)
    if expected == actual:
        print("PASS letter.py")
    else:
        print("FAIL letter.py")