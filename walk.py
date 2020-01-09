import os
import sys
from letter import IDService
from find_imports import ReadFileForImports


possible = {} 
cleaned = {} 
class FileNode:
    """ This will hold a file name. It might or might also not appear in different _trees_. """

    def __init__(self, short_name, file, full_name, letter, branch):
        self.short_name = short_name
        self.file = file
        self.letter = letter # The short ID - it will be used in the UI, not this file.
        
        self.paths = {}
        self.paths[branch] = full_name   
        self.imports = {} 
        self.imports[branch] = []
        
    def addNode(self, short_name, full_name, branch):
        #self.paths.append(short_name)
        self.paths[branch] = full_name
        self.imports[branch] = []


    def addImports(self, full_path, imports):
        self.imports[full_path] = imports


    def display(self):
        for full_name in self.paths:
            print("{}   {}   {}" .format(self.letter, full_name, self.short_name ))
            for key in self.imports:
                # print("\t\t{} :: {}".format(key, self.imports[key]))
                imported = self.imports[key]
                for item in imported:
                    if item in cleaned:
                        print( "YAY\t\t{} : {}".format(key, item))
                    else:
                        print( "BOO\t\t{} : {}".format(key, item))


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




def step1_read_dirs(dirs):
    id = IDService()
    for branch in dirs:
        for root, dirs, files in os.walk(branch):
            path = root.split(os.sep)
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx"):        
                    short_name = buildShortName(path, file, "src")
                    full_name = buildFullName(path, file)
                    if short_name in possible:
                        possible[short_name].addNode(short_name, full_name, branch)
                    else:
                        letter = id.label_gen()
                        node = FileNode(short_name, file, full_name, letter, branch)
                        possible[short_name] = node

starting_points = [] 
starting_points.append("./data1/")
starting_points.append("./data2/")
step1_read_dirs(starting_points)

def step2_find_imports():
    rffi = ReadFileForImports()
    for key in possible:
        node = possible[key]
        for full_path in node.paths:
            # print("full {} --- {} ".format(full_path, node.paths[full_path] ))
            path = node.paths[full_path]
            imports = rffi.readFileForImports(path)
            node.addImports(full_path, imports)
        # node.display()
step2_find_imports()

def cleanPossible():
    for key in possible:
        key = key.replace(".jsx", "")
        key = key.replace(".js", "")
        cleaned[key]="Oh - I wish I knew how a Set() object worked in python."

cleanPossible()


def show(): 
    for key in possible:
        node = possible[key]
        node.display()
show()

for c in cleaned:
    print(c )