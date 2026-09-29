try:
    file=open('new.txt',"r")
    print(file.read())
    file.close()
except FileNotFoundError :
    print('file not found')