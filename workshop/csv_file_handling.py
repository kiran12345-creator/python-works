# import csv
# f1=open('new.csv','w',newline='')
# content=\
# [
#     ['name','place','age'],
#     ['arun','ekm','23'],
#     ['amal','tvm','24']
# ]
# w=csv.writer(f1)
# w.writerows(content)
# f1.close()
#
# f=open('new.csv','r')
# r=csv.reader(f)
# for i in r:
#     print(i[2])
# f.close()
from csv import *
f1=open('data.csv','w')
content=[  ['name','place','age'],
    ['arun','ekm','23'],
    ['amal','tvm','24']]
w=writer(f1)
w.writerows(content)