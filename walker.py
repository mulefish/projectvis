import os


def getImports(path, startingDir):
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
                step1 = step1.replace("..","")
                step1 = step1.replace(";","")
                step1 = step1.replace("'","")
                #step1 = step1.replace(".\/", "!!")
                # step1 = step1.replace(".\\", "")
                # step1 = step1.replace("/", "")
                # step1 = step1.replace(".", "")

                step1 = step1.strip()
                #step1 = step1.replace("/", os.sep)
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
                #result = startingDir + step2 + os.sep + step1
                result = step2 + os.sep + step1
                results.append(result)
            line = fp.readline()
    return results





beginingPath = "./data1/src/"
for dirpath, dirs, files in os.walk(beginingPath):	
    for filename in files:

        if filename.endswith(".js") or filename.endswith(".jsx") or filename.endswith(".py"):
            fname = os.path.join(dirpath,filename)
            cleanFname = fname.replace(beginingPath, "")
            cleanFname = cleanFname.replace(".js", "")
            cleanFname = cleanFname.replace(".jxs", "")
            cleanFname = cleanFname.replace(".py", "")

            imports = getImports(fname, beginingPath)
            if len(imports) > 0:
                print("\t................\n{} ".format(cleanFname))
                for item in imports:
                    print(item)


