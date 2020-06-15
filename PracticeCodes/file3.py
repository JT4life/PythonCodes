import shutil

fileName1 = input("Enter file 1 name")

if fileName1 == "exit":
    exit();

else:
    fileName2 = input("enter 2nd file name")
    fileName3 = input("Create a newfile to merge")
    print();
    print("Both files are in ", fileName3)
    with open(fileName3,"wb") as wfd:
        for f in [fileName1,fileName2]:
            with open(f, "rb") as fd:
                shutil.copyfileobj(fd,wfd,700*700*10)
    c = open(fileName3,"r")
    print(c.read())
    c.close()
    
