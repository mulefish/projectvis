import os
import sys
from letter import IDService
from find_imports import ReadFileForImports

possible = {}

def clean_the_path(path_to_file):
    # get ./data1/src/components/Profile.js
    # return data1/src/components/Profile
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
                    file = clean_the_path(file)     
                    
                    if file in possible:
                        possible[file] += 1
                    else:
                        possible[file] = 1

rffi = ReadFileForImports()
def step2_read_dirs(dirs):
    for branch in dirs:
        for root, dirs, files in os.walk(branch):
            path = root.split(os.sep)
            print("...")
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx"):        
                    sep = "/"
                    path_to_file = sep.join(path) 
                    path_to_file += sep + file
                    # sprint( "{} |{}| {} {}".format(path, path_to_file, file, root))
                    imports = rffi.readFileForImports(path_to_file)
                    cleaned = clean_the_path(path_to_file)
                    print(">>>{}".format(cleaned))
                    for importedRef in imports:
                        path_to_ref = findAbsPath(root, importedRef)
                        ref = path_to_ref.split(os.sep)[-1]
                        if ref in possible:
                            print("\tYAY.....>{} and {}".format(path_to_ref, ref))
                        #else:
                        #    print("\tBOO.....>{} and {}".format(path_to_ref, ref))
                    


if __name__ == "__main__":
    starting_points = [] 
    starting_points.append("./data1/")
    starting_points.append("./data2/")
    step1_populate_possible_refs(starting_points)
    step2_read_dirs(starting_points)
