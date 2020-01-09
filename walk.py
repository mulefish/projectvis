import os
import sys
from letter import IDService
from find_imports import ReadFileForImports




class FileNode:
    """ This will hold a file name. It might or might also not appear in different _trees_. """

    def __init__(self, short_name, file, full_name, letter):
        self.paths = []
        self.short_name = short_name
        self.file = file
        self.letter = letter 
        #self.paths.append(short_name)        
        self.paths.append(full_name)        
        
    def addNode(self, short_name, full_name):
        #self.paths.append(short_name)
        self.paths.append(full_name)

    def display(self):
        for full_name in self.paths:
            print("\tID {}   path {} for {}" .format(self.letter, full_name, self.short_name ))


def buildShortName(path, filename, delimiter):
    """ 
    CONVERT 
    ['.', 'data2', 'src', 'components', 'Article'] CommentContainer.js 
    TO
    components/Article/CommentContainer.js
    """    
    result = ""
    flag = False
    for dir in path:
        if flag == True:
            result += dir + "/"
        if dir == delimiter:
            flag = True
    result += filename
    return result

def buildFullName(path, filename):
    """ 
    CONVERT 
    ['.', 'data2', 'src', 'components', 'Article'] CommentContainer.js 
    TO
    ./data2/src/components/Article/CommentContainer.js
    """    

    result = ""
    for dir in path:
        result += dir + "/"
    result += filename
    return result




possible = {} 
def step1_read_dirs(dirs):
    id = IDService()
    for dir in dirs:
        for root, dirs, files in os.walk(dir):
            path = root.split(os.sep)
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx"):        
                    short_name = buildShortName(path, file, "src")
                    full_name = buildFullName(path, file)
                    if short_name in possible:
                        possible[short_name].addNode(short_name, full_name)
                    else:
                        letter = id.label_gen()
                        node = FileNode(short_name, file, full_name, letter)
                        possible[short_name] = node

starting_points = [] 
starting_points.append("./data1/")
starting_points.append("./data2/")
step1_read_dirs(starting_points)



for key in possible:
    x = possible[key]
    x.display()