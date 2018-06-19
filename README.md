# Batch-Rename-Python
A simple python program used to change the name of files.

```python
import os
import time

def main():
    path = raw_input("Enter the path for the folder containing files to be renamed: ");
    
    try:
        for fileName in os.listdir(path):
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
```

　
