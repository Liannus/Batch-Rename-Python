# Batch -Rename-Python
# Josh Gorman   June 19 2018    Python 2.715 Anaconda   
# Places an underscore at the 5th position in the filename,
# pushes rest of name back one position.

# For ease of use in file explorer navigate to directory
# then right click on current location in nav bar and "copy address as text"
# then paste for command line argument.

import os
import time

def main():
    path = raw_input("Enter the path for the folder containing files to be renamed: ");
    
    try:
        for fileName in os.listdir(path):
            #----------------- Editable Code --------------------#
            #This can be changed to effect how the file is renamed
            #Its current state adds an underscore to position 5
            dst = fileName[:5] + "_" + fileName[5:]
            src = path + "\\" + fileName
            dst = path + "\\" + dst
            os.rename(src,dst);

        print("\n\nFiles renamed successfully")

    except WindowsError, e:
        print(e)


    print "Closing in 5 seconds..."
    var = time.sleep(5)

if __name__ == "__main__":
    main()
