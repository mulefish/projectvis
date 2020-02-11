from letter import IDService
from walker import ReadProject
from find_imports import ReadFileForImports
from caller import Caller

judge = Caller()         
readProject = ReadProject()
readFileForImported = ReadFileForImports()

def test_idea_manipulation():
    a = ['a', 'b', 'c', 'd', 'e', 'f']
    actual = a[:-1]
    expected = ['a', 'b', 'c', 'd', 'e']
    judge.verdict(expected, actual)

def test_read_imports_from_React_file_figureOutPath():
    f = "./data1/src/components/App.js"
    startingDir = "src"
    actual = readFileForImported.readFileForReactImports(f, startingDir)
    expected = ['src/components/Home','src/components/Login','src/components/Profile','src/components/ProfileFavorites','src/components/Register','src/components/something/FINDME','src/store','src/react-router-redux']
    # for x in actual: 
    #     print( x )
    judge.verdict(expected, actual)

def test_readProject_clean_the_path():
    given = "./data1/src/components/Profile.js"
    expected = "src/components/Profile"
    branch = "data1"
    # actual = readProject.clean_the_path(given, branch) 
    actual = readProject.clean_the_path(given, "src") 
    print( "actual is!\n {}".format(actual ))
    judge.verdict(actual, expected)




def test_readProject_fictional_and_actual_merge():

    """Given 2 nearly identical branches for a project, 
    suppose they both contain a "/foo/bar/baz/somefile.js" - this will be the 'fictional' file
    In reality, these two files will be at something like: 
    /Users/kermitt/playground/projectvis/data1/src/foo/bar/baz/somefile.js 
    and 
    /Users/kermitt/playground/projectvis/data2/src/foo/bar/baz/somefile.js
    I will consider these latter two to be the 'actual' 
    """ 

    starting_points = [] 
    starting_points.append("data1")
    starting_points.append("data2")
    readProject.step1_populate_possible_refs(starting_points)

    # Most of the possible will be seen twice - In the dummy data only FINDME ought to be 1 
    actual1 = 0
    for key in readProject.possible:
        val = readProject.possible[key]

    actual1 = readProject.possible["src/components/Article/FINDME"]
    actual2 = readProject.possible["src/components/ListErrors"]
    actual3 = readProject.possible["src/components/Article/CommentContainer"]
    expected1 = 1
    expected2 = 2
    expected3 = 2
    isOk = actual1 == expected1 and  actual2 == expected2 and  actual3 == expected3
    judge.verdict( True, isOk)


def test_letter_IDService():

    """Letters > Numbers ( as far as IDs go ) """

    id = IDService()
    letter1 = id.label_gen()
    letter2 = id.label_gen()
    letter3 = id.label_gen()
    expected = "a b c" 
    actual = "{} {} {}".format(letter1, letter2, letter3)
    judge.verdict(actual, expected)


if __name__ == '__main__':

    test_idea_manipulation()
#    test_readProject_clean_the_path()
#    test_readProject_fictional_and_actual_merge()
    test_letter_IDService()
    test_read_imports_from_React_file_figureOutPath()