import os
import re
 

def getImports(path, startingDir):
    # "data1/src/dir/file.js" ought to be "dir/"
    tmp = path.split(startingDir)[1] # toss the 'data1' 
    pieces = tmp.split(os.sep) # split into list
    pieces = pieces[:-1] # toss the 'file.js

    results = []
    with open(path) as fp:
        line = fp.readline()
        while line:
            #if "import" in line and "from" in line:
            if "from " in line:
                step1 = line.strip()
                step1 = step1.split("from")[1]
                step1 = step1.replace("..","")
                step1 = step1.replace(";","")
                step1 = step1.replace("'","")
                step1 = step1.strip()
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
                step1 = step1.replace("/","|")
                pathToHere = pieces[:-1]
                step2 = os.sep
                step2 = step2.join(pathToHere)
                #result = startingDir + step2 + os.sep + step1
                result = step2 + os.sep + step1
                result = result.replace("/","|")
                result = result.replace("\\","|")
                # result = result.replace("||","QQ")
                while "||" in result:
                    result = result.replace("||", "|")
                result = result.replace(".|","")
                if result[0] == "|":
                    result = "remove" + result 
                    result = result.replace("remove|", "")
                
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
            cleanFname = cleanFname.replace("\\","|")
            cleanFname = cleanFname.replace("/","|")
            imports = getImports(fname, beginingPath)
            if len(imports) > 0:
                print("\t................\n{} ".format(cleanFname))
                for item in imports:


                    print(item)


