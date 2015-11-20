'''
Useful functions for file system
'''

import os 

# Get the path of current working directory
os.getcwd()

# See files in the current working directory
os.listdir()
# Alternative way
os.listdir(os.curdir)
# In IPython
pwd

# Change working directory
os.chdir("Python")

# Create path without using specific syntax for operating system
# As you may know, the path from Windows and Unix system will be different
# Windows is by backslash \, while Unix uses /
print(os.path.join('bin', 'utils', 'disktools'))
### You will see bin\utils\disktools in Window
### You will see bin/utils/disktools in Unix

# More complicated example
path1 = os.path.join('mydir', 'bin')
path2 = os.path.join('utils', 'disktools', 'chkdisk')
print(os.path.join(path1, path2))

# Get the basename(file) or directory name(folder)
os.path.basename(os.path.join('some', 'directory', 'path.jpg'))
os.path.dirname(os.path.join('some', 'directory', 'path.jpg'))

# Operating System
import sys
sys.platform

# Information about file
# Check whether the path exists
os.path.exists('C:\\Documents and Settings\\jason\\My Documents')
# Check whether the path is a directory
os.path.isdir('C:\\Documents and Settings\\jason\\My Documents')
# Check whether the path is a file
os.path.isfile('C:\\Documents and Settings\\jason\\My Documents')

# To rename file
os.rename('registry.bkp', 'registry.bkp.old')
# To remove file, cannot remove directory, use os.rmdir to remove directory
os.remove('book1.doc.tmp')


'''
Reading and writing files
'''

# Open function: create a handler(connection) with file
fhand = open('mbox-short.txt', 'r')
for line in fhand:
	# Remove \n at the end of each line
	line = line.rstrip()
	print(line)

# You can also use readline function to read line by line
# Note that you have to restart the connection 
fhand = open('mbox-short.txt', 'r')
# It will only read in one line
myfile = fhand.readline()
print(myfile)

# Or use read to read in all the line, it will return a string
fhand = open('mbox-short.txt', 'r')
myfile_str = fhand.read()
print(myfile_str)
type(myfile_str)

# Or use readlines to read in all the line, it will return a list
# Each element in the list is one line
fhand = open('mbox-short.txt', 'r')
myfilelist = fhand.readlines()
print(myfilelist)
type(myfilelist)

# A quick way to examine how many line in the file
fhand = open('mbox-short.txt', 'r')
count = 0
for line in fhand:
	count = count + 1

count
# Alternative way
fhand = open('mbox-short.txt', 'r')
count = 0
while fhand.readline() != '':
	count = count + 1

count

# You can specify the newline character when you read in the data
input_file = open('myfile', newline='\n')

# You can use input function to let user give the input to your program
# It will always read the input as string. Sometime, you may need to transform it into float. 
x = input("enter file name to use: ")
x 

'''
Pickle
'''
import pickle
# If you want to save your variable and recall it late,
# you can use the pickle module to do this
file = open("state", 'w')
pickle.dump(a, file)
pickle.dump(b, file)
pickle.dump(c, file)
file.close()

# When you want to get back your data, use load to read them in
file = open("state", 'r')
a = pickle.load(file)
b = pickle.load(file)
c = pickle.load(file)
file.close()