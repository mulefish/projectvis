import json
import os

class ReadFileForImports:
    
    def readFileForPythonImports(self, path, startingDir):
        print("WRITE THIS! readFileForPythonImports()")
        return False

    def readFileForReactImports(self, path, startingDir):
        # "data1/src/dir/file.js" ought to be "dir/file.js"
        tmp = path.split(startingDir)[1] 
        pieces = tmp.split(os.sep)
        results = []
        with open(path) as fp:
            line = fp.readline()
            while line:
                if "import" in line and "from" in line:
                    result = line.strip()
                    # import { SET_PAGE } from '../constants/actionTypes';
                    result = result.split("from")[1]
                
                    # '../constants/actionTypes';
                    result = result.replace(";","")
                    result = result.replace("'","")
                    result = result.strip()
                    
                    # ../constants/actionTypes
                    results.append(result)

                line = fp.readline()

        for r in results:
            ary = r.split(os.sep)
            # p rint(r)  
            # p rint(tmp)
            # p rint(pieces)
            # p rint(ary)
            # p rint('-')  
        return results

if __name__ == "__main__":
    """Self test"""
    # p = "data1/react-redux-realworld-example-app-master/src/components/ListPagination.js"
    p = "./data1/src/components/App.js"
    rffi = ReadFileForImports()
    results = rffi.readFileForReactImports(p, "src")
    actual = json.dumps(results)
    print( actual )    
