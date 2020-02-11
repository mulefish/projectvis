import json
import os

class ReadFileForImports:
    
    def readFileForPythonImports(self, path, startingDir):
        print("WRITE THIS! readFileForPythonImports()")
        return False

    def readFileForReactImports(self, path, startingDir):
        # "data1/src/dir/file.js" ought to be "dir/"
        tmp = path.split(startingDir)[1] # toss the 'data1' 
        pieces = tmp.split(os.sep) # split into list
        pieces = pieces[:-1] # toss the 'file.js

        results = []
        with open(path) as fp:
            line = fp.readline()
            while line:
                if "import" in line and "from" in line:
                    step1 = line.strip()
                    # import { SET_PAGE } from '../constants/actionTypes';
                    step1 = step1.split("from")[1]
                    # '../constants/actionTypes';
                    step1 = step1.replace(";","")
                    step1 = step1.replace("'","")
                    step1 = step1.strip()
                    
                    # ../constants/actionTypes
                    ary = step1.split(os.sep)
                    goUp = 0 
                    ary2 = [] 
                    for item in ary:
                        if item == "..":
                            # skip this!
                            goUp -= 1
                        else:
                            # rebuild this array 
                            ary2.append(item)

                    step1 = os.sep.join(ary2)
                    pathToHere = pieces[:-1]
                    step2 = os.sep
                    step2 = step2.join(pathToHere)

                    result = startingDir + step2 + os.sep + step1

                    results.append(result)

                line = fp.readline()

        return results

if __name__ == "__main__":
    """Self test"""
    # p = "data1/react-redux-realworld-example-app-master/src/components/ListPagination.js"
    p = "./data1/src/components/App.js"
    rffi = ReadFileForImports()
    results = rffi.readFileForReactImports(p, "src")
    actual = json.dumps(results)
    print( actual )    