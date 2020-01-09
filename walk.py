import os
import sys
from letter import IDService



class FileNode:
    """ This will hold a file name. It might or might also not appear in different _trees_. """

    def __init__(self, full_path, letter, filename, short_path):
        self.paths = []
        self.paths.append(full_path)        
        self.letter = letter
        self.filename = filename
        self.short_path = short_path

    def addAnotherFullPath(self, full_path):
        if full_path not in self.paths:
            self.paths.append(full_path)

    def display(self):
        n = len(self.paths)
        print("{} {} {}".format(n, self.letter, self.short_path))
        for item in self.paths:
            print("\t|{}|".format( item ))


walk_dirs = []
# walk_dirs.append("data1") # sys.argv[1] # Compare this 
# walk_dirs.append("data2") # sys.argv[1] # to this

walk_dirs.append("data1/react-redux-realworld-example-app-master/src") # sys.argv[1] # Compare this 
walk_dirs.append("data2/react-redux-realworld-example-app-master/src") # sys.argv[1] # Compare this 



possible = {}

def step1_read_dirs(ary):
    id = IDService()

    for walk_dir in ary:


        for root, subdirs, files in os.walk(walk_dir):
            print("{}    {}".format( walk_dir, root ))
            for subdir in subdirs:
                k = 0 
                for filename in files:
                    if filename.endswith(".jsx") or filename.endswith(".js"):
                        full_path = os.path.join(root, filename)
                        short_path = full_path
                        # short_path = short_path.replace(walk_dir + "/",  "|")
                        short_path = full_path.split("src/")[1]

                        
                        if short_path in possible:
                            # Seen this file before! But in a different tree
                            possible[short_path].addAnotherFullPath(full_path)
                        else:
                            letter = id.label_gen()
                            fn = FileNode(full_path, letter, filename, short_path)
                            possible[short_path] = fn

step1_read_dirs(walk_dirs)
for key in possible:
    possible[key].display()



