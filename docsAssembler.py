import docx
import os

def getAllDocx(directory = os.getcwd()):
    files = []
    for f in os.listdir(directory):
        if f.endswith('.docx') or f.endswith('.doc') or f.endswith('.odt'):
            files.append(f)
    return files
print(getAllDocx('/home/deus'))