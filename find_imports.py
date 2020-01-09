import json

class ReadFileForImports:
    
    def readFileForImports(self, path):
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
        return results

if __name__ == "__main__":
    """Self test"""
    p = "data1/react-redux-realworld-example-app-master/src/components/ListPagination.js"
    rffi = ReadFileForImports()
    results = rffi.readFileForImports(p)
    actual = json.dumps(results)
    expected = json.dumps(["react","../agent","react-redux","../constants/actionTypes"])
    
    if expected == actual:
        print("PASS find_imports.py")
    else:
        print("FAIL find_imports.py")