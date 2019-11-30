import os
import re
dir = "C:/Python-Practice/Day4"
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.log'):
            
            
            fo=open(file,"r")
            data=fo.read()
            pattern='[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
            matches=re.finditer(pattern,data)
            if matches:
                
                print ("EmailIds from file =>",file)
                for match in matches:
                    print(data[match.start():match.end()])