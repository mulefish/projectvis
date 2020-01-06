import os
import sys

walk_dir = "data" # sys.argv[1]
#print('walk_dir = ' + walk_dir)
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)

    for subdir in subdirs:
        print('\t- subdirectory ' + subdir)
        k = 0 
        for filename in files:
            if filename.endswith(".jsx") or filename.endswith(".js"):
                file_path = os.path.join(root, filename)
                k += 1
                print('\t {} : file {} (full path: {})'.format(k, filename, file_path))



p = "data/react-redux-realworld-example-app-master/src/components/ListPagination.js"

def readFileForImports(path):
    with open(path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if "import" in line and "from" in line:
                print("Line {}: {}".format(cnt, line.strip()))

            line = fp.readline()
                
            cnt += 1


readFileForImports(p)



