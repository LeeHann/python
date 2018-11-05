from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile=askopenfileaname()
if (readFile != None):
    infile=open(readFile,"r")
for line in infile.readlines():
    line=line.rstrip()
    print(line)
infile.close()
