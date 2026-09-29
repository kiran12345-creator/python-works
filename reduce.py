def file_open():
    f1=open('new.txt','r')
    content=f1.read()
    print(content)
    f1.close()
def write_file():
    f2=open('new.txt','w')
    content=input('enter content to be written')
    f2.write(content)
    print('new.txt')
    f2.close()
write_file()