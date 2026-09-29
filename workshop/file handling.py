import os
def file_open():
    f1=open('../exception/new.txt', 'r')
    content=f1.read()
    print(content)
    f1.close()
def write_file():
    f2=open('../exception/new.txt', 'w')
    content=input('enter content to be written')
    f2.write(content)
    print('new.txt')
    f2.close()
def append_file():
    f3=open('../exception/new.txt', 'a')
    content=input('enter content to append')
    f3.write(content)
    f3.close()
def delete():

    filename=input('enter file name')
    f4 = open('filename', 'r')
    os.remove(filename)
    f4.close()

def search():
    filename=input('enter file name')
    f5=open('filename','r')
    content=f5.read()
    key=input('enter word to be searched')
    if key in content:
        print('key found')
    else:
        print('word not found')
while(True):
    print('1. open')
    print('2.read')
    print('3.write')
    print('4.remove')
    print('5.exit')
    ch=int(input('enter your choice'))

    if ch==1:
        file_open()
    elif ch==2:
        write_file()
    elif ch==3:
        append_file()
    elif ch==4:
        delete()
    elif ch==5:
        search()
    else:
        exit()



