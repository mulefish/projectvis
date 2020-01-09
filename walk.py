import os
import sys
from letter import IDService
from find_imports import ReadFileForImports

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



rffi = ReadFileForImports()
def step1_read_dirs(dirs):
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
                        ref = findAbsPath(root, importedRef)
                        print(".....>{}".format(ref))
                    


if __name__ == "__main__":
    starting_points = [] 
    starting_points.append("./data1/")
    starting_points.append("./data2/")
    step1_read_dirs(starting_points)
