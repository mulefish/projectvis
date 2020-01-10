from walker import *
from letter import IDService

def findImportPath_noChange():
    path_to_file = "a/b/c/d"
    relative_path_of_the_import = "/kittycat/something"
    expected = "a/b/c/d/kittycat/something"
    actual = findAbsPath(path_to_file, relative_path_of_the_import)

    if actual == expected:
        print("PASS actual |{}| for findImportPath_noChange".format(actual))
    else:
        print("FAIL actual |{}| for findImportPath_noChange".format(actual))

def findImportPath_up2dirs():
    path_to_file = "a/b/c/d"
    relative_path_of_the_import = "../../something"
    expected = "a/b/something"
    actual = findAbsPath(path_to_file, relative_path_of_the_import)

    if actual == expected:
        print("PASS actual |{}| for findImportPath_up2dirs".format(actual))
    else:
        print("FAIL actual |{}| for findImportPath_up2dirs".format(actual))

def findImportPath_up1dir():
    path_to_file = "a/b/c/d"
    relative_path_of_the_import = "../kittycat/finch/something"
    expected = "a/b/c/kittycat/finch/something"
    actual = findAbsPath(path_to_file, relative_path_of_the_import)

    if actual == expected:
        print("PASS actual |{}| for findImportPath_up1dir".format(actual))
    else:
        print("FAIL actual |{}| for findImportPath_up1dir".format(actual))


def findImportPath_up1dir_withLeadingDot():
    path_to_file = "a/b/c/d"
    relative_path_of_the_import = "./../kittycat/finch/something"
    expected = "a/b/c/kittycat/finch/something"
    actual = findAbsPath(path_to_file, relative_path_of_the_import)

    if actual == expected:
        print("PASS actual |{}| for findImportPath_up1dir_withLeadingDot".format(actual))
    else:
        print("FAIL actual |{}| for findImportPath_up1dir_withLeadingDot".format(actual))

def clean_the_path_doSomething():
    branch = "data1/"
    given = "./data1/src/components/Profile.js"
    expected = "src/components/Profile"
    actual = clean_the_path(given, branch)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_test".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_test".format(actual))

def clean_the_path_doNothing():
    branch = "data1/"
    given = "src/components/Profile"
    expected = "src/components/Profile"
    actual = clean_the_path(given, branch)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_doNothing".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_doNothing".format(actual))

def clean_the_path_of_jsx_extension():
    branch = "data1/"
    given = "src/components/Profile.jsx"
    expected = "src/components/Profile"
    actual = clean_the_path(given, branch)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_of_jsx_extension".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_of_jsx_extension".format(actual))

def letter_test():
    id = IDService()
    letter1 = id.label_gen()
    letter2 = id.label_gen()
    letter3 = id.label_gen()
    expected = "a b c"
    actual = "{} {} {}".format(letter1, letter2, letter3)
    if actual == expected:
        print("PASS actual |{}| for letter_test".format(actual))
    else:
        print("FAIL actual |{}| for letter_test".format(actual))

def find_imported_ref_and_discard_the_path_test1():
    given = "a/b/c/d/something"
    expected = "something"
    actual = given.split(os.sep)[-1]
    if actual == expected:
        print("PASS actual |{}| for find_imported_ref_and_discard_the_path_test1".format(actual))
    else:
        print("FAIL actual |{}| for find_imported_ref_and_discard_the_path_test1".format(actual))

def find_imported_ref_and_discard_the_path_test2():
    given = "something"
    expected = "something"
    actual = given.split(os.sep)[-1]
    if actual == expected:
        print("PASS actual |{}| for find_imported_ref_and_discard_the_path_test2".format(actual))
    else:
        print("FAIL actual |{}| for find_imported_ref_and_discard_the_path_test2".format(actual))


print("****")
findImportPath_noChange()
findImportPath_up2dirs()
findImportPath_up1dir()
findImportPath_up1dir_withLeadingDot()
clean_the_path_doSomething()
clean_the_path_doNothing()
clean_the_path_of_jsx_extension()
letter_test()
find_imported_ref_and_discard_the_path_test1()
find_imported_ref_and_discard_the_path_test2()
print("****")
