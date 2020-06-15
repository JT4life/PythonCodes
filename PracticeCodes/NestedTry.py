#Nested Try
try:
    fh = open("ABCD.txt", "w")
    try:
        fh.write("This is my test file")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error : cant find File!")
