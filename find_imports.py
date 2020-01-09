p = "data1/react-redux-realworld-example-app-master/src/components/ListPagination.js"

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