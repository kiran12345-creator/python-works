from json import *
# f1=open('filename.json','w')
# content=[{"name":'amal'}]
# dump(content,f1)
# f1.close()

f2=open('new.json','r')
content=load(f2)
print(content)
f2.close()