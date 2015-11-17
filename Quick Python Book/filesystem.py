'''
Useful function for file system
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

