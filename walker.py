




import os
import sys
from letter import IDService
from find_imports import ReadFileForImports
import json
import os.path


idService = IDService()
SEP = os.sep 
readFileForImported = ReadFileForImports()

class ReadProject:

    def __init__(self):
        self.startingDir = "src"
        self.possible = {}

    def clean_the_path(self, path_to_file, startingDir):

        #print("ONE {}".format( path_to_file ))

        path_to_file = os.path.splitext(path_to_file)[0]
        #print("TWO {}".format( path_to_file ))
        path_to_file = path_to_file.split(startingDir + os.sep)[1]
        #print("THREE {}".format( path_to_file ))
        # print()
        return path_to_file
    # def clean_the_path(self, path_to_file, branch):
    #     path_to_file = os.path.splitext(path_to_file)[0]
    #     path_to_file = path_to_file.split(branch + os.sep)[1]
    #     return path_to_file
    def step1_populate_possible_refs(self, dirs):
        # Populate a hash of possible refs. If there is a ref made and 
        # it is not in the 'possible' dict then that is a ref to some 3rd party thing, 
        # such as 'react' or 'font-awesome' or something
        for branch in dirs:
            for root, dirs, files in os.walk(branch):
                for file in files:

                    absFile = "{}{}{}".format(root, SEP, file)
                    if absFile.endswith(".js") or absFile.endswith(".jsx"):   
                        absFile = self.clean_the_path(absFile, branch)     
                        if absFile in self.possible:
                            self.possible[absFile] += 1
                        else:
                            self.possible[absFile] = 1


if __name__ == "__main__":
    starting_points = [] 
    starting_points.append("data1")
    starting_points.append("data2")
    readProject = ReadProject()
    readProject.step1_populate_possible_refs(starting_points)

    for key in readProject.possible:
        count = readProject.possible[key]
        print( "SELF-TEST: {}   |{}| ".format(count, key ))


        #startingDir = "src"
        #actual = readFileForImported.readFileForReactImports(f, startingDir)

        