def remove_space(text):
    temp=""
    for i in text:
        if i != " "  :
            temp=temp+i
    return temp
print(remove_space("hello world"))