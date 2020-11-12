import re
import numpy as np

def readinLine(line):
    runNo = re.search('run_0(\d)',line)
    terms = line.split()
    print(terms)
    Xsec = eval(terms[3])
    XsecErrorBar = eval(terms[6])
    return runNo,Xsec,XsecErrorBar


def readinXsec(path):
    Xseces = []
    XsecErrorBars = []
    with open(path+"/crossx.html") as f:
        lines = f.readlines()
        templateStr = re.compile(r'        <td rowspan=1><center><a href="./HTML/run_0(\d)/results.html"> ((\d+\.\d+)(e-\d+)*) <font face=symbol>&#177;</font> ((\d+\.\d+)(e-\d+)*) </a>  </center></td>')
        for line in lines:
            if templateStr.match(line):
                run,Xsec,XsecErrorBar = readinLine(line)
                Xseces.append(Xsec)
                XsecErrorBars.append(XsecErrorBar)
    return np.asarray(Xseces),np.asarray(XsecErrorBars)