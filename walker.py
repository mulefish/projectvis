import os
import sys
from letter import IDService
from find_imports import ReadFileForImports
import json

class Virtual:
    def __init__(self, fictionalAbs ):
        self.fictionalAbs = fictionalAbs # e.g., 'components/reducers/Logic.js'




possible = {}
nodes = {} 
idService = IDService()
SEP = os.sep 
THIS_DIR = "." + SEP
UP_DIR = ".." + SEP
class Node:
    def __init__(self, branch, path_to_file, letter, depth):
        self.refs = {}
        self.path_to_file = path_to_file
        self.letter = letter
        self.depth = depth # a/b/c/something.js = 3 but a/b/c/d/e/f/something-else.js = 6  
        
def clean_the_path(path_to_file, branch):
    # get ./data1/src/components/Profile.js
    # return data1/src/components/Profile
    # path_to_file = path_to_file.replace(branch, "")
    # path_to_file = path_to_file.replace(".jsx", "")
    # path_to_file = path_to_file.replace(".js", "")
    # path_to_file = path_to_file.replace(THIS_DIR, "")
    return path_to_file

def step1_populate_possible_refs(dirs):
    # Populate a hash of possible refs. If there is a ref made and 
    # it is not in the 'possible' dict then that is a ref to some 3rd party thing, 
    # such as 'react' or 'font-awesome' or something
    for branch in dirs:
        for root, dirs, files in os.walk(branch):
            for file in files:

                absFile = "{}{}{}".format(root, SEP, file)
                if absFile.endswith(".js") or absFile.endswith(".jsx"):   
                    absFile = clean_the_path(absFile, branch)     
                    if absFile in possible:
                        possible[absFile] += 1
                    else:
                        possible[absFile] = 1

# rffi = ReadFileForImports()
# def step2_read_dirs(dirs):
#     for branch in dirs:
#         for root, dirs, files in os.walk(branch):
#             path = root.split(os.sep)
#             # print("...")
#             for file in files:
#                 if file.endswith(".js") or file.endswith(".jsx"):        
#                     sep = "/"
#                     path_to_file = sep.join(path) 
#                     path_to_file += sep + file
#                     imports = rffi.readFileForImports(path_to_file)
#                     cleaned = clean_the_path(path_to_file, branch)
#                     if cleaned not in nodes:
#                         letter = idService.label_gen()
#                         node = Node(branch, cleaned, letter, len(path))
#                         nodes[cleaned] = node
#                     good = []
#                     bad = []
#                     for importedRef in imports:
#                         path_to_ref = findAbsPath(root, importedRef)
#                         ref = path_to_ref.split(os.sep)[-1]
#                         if ref in possible:
#                             good.append(path_to_ref)
#                         else:
#                             bad.append(path_to_ref)
#                     nodes[cleaned].addRefsForThisBranch(branch, good)                    

# def show3_show():
#     for key in nodes:
#         node = nodes[key]
#         node.display()

# def step3_emit_to_file_as_json():
#     info = {}
#     for key in nodes:
#         node = nodes[key]
#         letter = node.letter
#         ref = node.refs
#         depth = node.depth

#         info[key] = {}
#         info[key]['letter'] = letter
#         info[key]['ref'] = ref
#         info[key]['depth'] = depth
#     file='data.js' 
#     with open(file, 'w') as filetowrite:
#         filetowrite.write("const data = {}".format(json.dumps(info)))

#     # print( json.dumps(info))
#     for x in info:
#         print(x)
#     print("\n*** Wrote to {} ***\n".format(file))


if __name__ == "__main__":
    starting_points = [] 
    starting_points.append("./data1/")
    starting_points.append("./data2/")
    step1_populate_possible_refs(starting_points)
    # step2_read_dirs(starting_points)
    # # show3_show()
    # step3_emit_to_file_as_json()

    for key in possible:
        value = possible[key]
        print( "{}   {} ".format(value, key ))
        