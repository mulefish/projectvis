from walker import *
from letter import IDService
import unittest
from walker import *

class TDD(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.readProject = ReadProject()

    def test_clean_the_path(self):
        given = "./data1/src/components/Profile.js"
        expected = "src/components/Profile"
        branch = "data1"
        actual = self.readProject.clean_the_path(given, branch) 
        self.assertEqual(actual, expected)

    def test_fictional_and_actual_merge(self):

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
        self.readProject.step1_populate_possible_refs(starting_points)

        # Most of the possible will be seen twice - In the dummy data only FINDME ought to be 1 
        actual1 = 0
        # print("...! ")
        for key in self.readProject.possible:
            val = self.readProject.possible[key]
       
        actual1 = self.readProject.possible["src/components/Article/FINDME"]
        actual2 = self.readProject.possible["src/components/ListErrors"]
        actual3 = self.readProject.possible["src/components/Article/CommentContainer"]
        expected1 = 1
        expected2 = 2
        expected3 = 2

        isOk = actual1 == expected1 and  actual2 == expected2 and  actual3 == expected3
        
        self.assertTrue(isOk)

       

    def test_letter(self):

        """Letters > Numbers ( as far as IDs go ) """

        id = IDService()
        letter1 = id.label_gen()
        letter2 = id.label_gen()
        letter3 = id.label_gen()
        expected = "a b c"
        actual = "{} {} {}".format(letter1, letter2, letter3)
        self.assertEqual(actual, expected)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

