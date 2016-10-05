import os
import re


def rename_file():
# Open the file directory and list out all files

    list_of_files = os.listdir(r"/Users/nishantisme/Desktop/alphabet")
    print (list_of_files)
    os.chdir(r"/Users/nishantisme/Desktop/alphabet")

# Rename all files
    for name in list_of_files:
        os.rename(name, re.sub("[0-9](?!\d*$)", "", name))
rename_file()
