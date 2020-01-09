from walk import *

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
    given = "./data1/src/components/Profile.js"
    expected = "data1/src/components/Profile"
    actual = clean_the_path(given)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_test".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_test".format(actual))

def clean_the_path_doNothing():
    given = "data1/src/components/Profile"
    expected = "data1/src/components/Profile"
    actual = clean_the_path(given)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_doNothing".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_doNothing".format(actual))

def clean_the_path_of_jsx_extension():
    given = "data1/src/components/Profile.jsx"
    expected = "data1/src/components/Profile"
    actual = clean_the_path(given)
    if actual == expected:
        print("PASS actual |{}| for clean_the_path_of_jsx_extension".format(actual))
    else:
        print("FAIL actual |{}| for clean_the_path_of_jsx_extension".format(actual))


print("****")
findImportPath_noChange()
findImportPath_up2dirs()
findImportPath_up1dir()
findImportPath_up1dir_withLeadingDot()
clean_the_path_doSomething()
clean_the_path_doNothing()
clean_the_path_of_jsx_extension()
print("****")
