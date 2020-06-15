import os
'''
def get(filename, mode):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            return file.readline()
    else:
        print("File not found")
        return None

a = get('fileOpen.txt','r')'''

def get(filename, mode):
    with open(filename, 'r') as file:
        if os.path.isfile(filename):
            return file.readline()
        else:
            print("File not found")
            return None

a = get('fileOpen.txt', 'r')
print(a)
