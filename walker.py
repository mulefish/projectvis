import os
import sys
from letter import IDService
from find_imports import ReadFileForImports

"""
1: Create a dataviz of a  well-formed REACT project. 
2: Nodes will be files inside the project. Each node will import zero or more other nodes from
inside this project. This will ignore imports from  outside of the project. These imported refs will be 
the edges. 
3: This will also be able to import 2 different versions. I am thinking branch1 vs. branch2 of a project. 
"""


possible = {}
nodes = {} 
idService = IDService()

class Node:
    def __init__(self, branch, path_to_file, letter):
        self.refs = {}
        self.path_to_file = path_to_file
        self.letter = letter
        
    def addRefsForThisBranch(self, branch, refArray):
        ary = [] 
        b = branch.replace("./", "")
        for ref in refArray:
            x = ref.replace(b, "")
            ary.append(x)
        self.refs[branch] = ary

    def display(self):
        print("ID {}    {}".format(self.letter, self.path_to_file))
        for branch in self.refs:
            for ref in self.refs[branch]:
                print("\t\t{}".format(ref))

def clean_the_path(path_to_file, branch):
    # get ./data1/src/components/Profile.js
    # return data1/src/components/Profile
    path_to_file = path_to_file.replace(branch, "")
    path_to_file = path_to_file.replace(".jsx", "")
    path_to_file = path_to_file.replace(".js", "")
    path_to_file = path_to_file.replace("./", "")
    return path_to_file

def findAbsPath(path_to_file, relative_path):
    #pathToFile = "a/b/c/d"
    #relative_path = "../../something"
    #expected = "a/b/something"
    count = relative_path.count("..", 0, len(relative_path))
    path = path_to_file.split(os.sep)
    sep = "/"
    #absolute = sep.join(path[:count]) # <--- I wanted this to work: The below seems clunky.
    n = len(path)
    n -= count
    absolute = ""
    for d in range(n):
        absolute += path[d] + sep
    
    absolute += relative_path.replace("../","")
    absolute = absolute.replace("//","/")
    absolute = absolute.replace("./","")

    return absolute

def step1_populate_possible_refs(dirs):
    # Populate a hash of possible refs. If there is a ref made and 
    # it is not in the 'possible' dict then that is a ref to some 3rd party thing, 
    # such as 'react' or 'font-awesome' or something
    for branch in dirs:
        for root, dirs, files in os.walk(branch):
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx"):   
                    file = clean_the_path(file, branch)     
                    
                    if file in possible:
                        possible[file] += 1
                    else:
                        possible[file] = 1

rffi = ReadFileForImports()
def step2_read_dirs(dirs):
    for branch in dirs:
        for root, dirs, files in os.walk(branch):
            path = root.split(os.sep)
            # print("...")
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx"):        
                    sep = "/"
                    path_to_file = sep.join(path) 
                    path_to_file += sep + file
                    imports = rffi.readFileForImports(path_to_file)
                    cleaned = clean_the_path(path_to_file, branch)
                    if cleaned not in nodes:
                        letter = idService.label_gen()
                        node = Node(branch, cleaned, letter)
                        nodes[cleaned] = node
                    good = []
                    bad = []
                    for importedRef in imports:
                        path_to_ref = findAbsPath(root, importedRef)
                        ref = path_to_ref.split(os.sep)[-1]
                        if ref in possible:
                            good.append(path_to_ref)
                        else:
                            bad.append(path_to_ref)
                    nodes[cleaned].addRefsForThisBranch(branch, good)                    

def show3_show():
    for key in nodes:
        node = nodes[key]
        node.display()

if __name__ == "__main__":
    starting_points = [] 
    starting_points.append("./data1/")
    starting_points.append("./data2/")
    step1_populate_possible_refs(starting_points)
    step2_read_dirs(starting_points)
    show3_show()