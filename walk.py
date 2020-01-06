import os
import sys
from letter import IDService

class FileDetails:

    def __init__(self, letter, path, file_name, root):
        self.letter = letter
        self.path = path
        self.file_name = file_name
        self.root = root 

    def display(self):
        print("ID {} PATH {} NAME {} ROOT {} ".format(self.letter, self.path, self.file_name, self.root ))


walk_dirs = []
walk_dirs.append("data") # sys.argv[1]
possible = {}
def read_dirs(ary):

    id = IDService()
    for walk_dir in ary:
        for root, subdirs, files in os.walk(walk_dir):
            #print('--\nroot = ' + root)

            for subdir in subdirs:
                #print('\t- subdirectory ' + subdir)
                k = 0 
                for filename in files:
                    if filename.endswith(".jsx") or filename.endswith(".js"):
                        full_path = os.path.join(root, filename)
                        k += 1
                        # print('\t! {} : file {} (full path: {})'.format(k, filename, full_path))
                        if full_path not in possible:
                            letter = id.label_gen()
                            fd = FileDetails(letter, full_path, filename, root)
                            possible[full_path] = fd


read_dirs(walk_dirs)

for key in possible:
    fd = possible[key]
    fd.display()

# p = "data/react-redux-realworld-example-app-master/src/components/ListPagination.js"

# def readFileForImports(path):
#     with open(path) as fp:
#         line = fp.readline()
#         cnt = 1
#         while line:
#             if "import" in line and "from" in line:
#                 print("Line {}: {}".format(cnt, line.strip()))

#             line = fp.readline()
                
#             cnt += 1


# readFileForImports(p)



