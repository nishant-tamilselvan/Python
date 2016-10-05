import os
import re


def rename_file():
# Open the file directory and list out all files

    list_of_files = os.listdir(r"/Users/nishantisme/Desktop/alphabet")
    # Print the names of all the files inside the specified directory
    print (list_of_files)
    # Change the current working directory to rename all the files.
    os.chdir(r"/Users/nishantisme/Desktop/alphabet")

# Rename all files
    for name in list_of_files:
        # will search and remove all the digits from the text
        os.rename(name, re.sub("[0-9](?!\d*$)", "", name))

# calling the function rename_file()
rename_file()
