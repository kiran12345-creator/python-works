#define a class named book
#attributes :title,author,price,pages,language
#methods:gettitle,getauthor,getprice,settitle,setauthor,setprice
class Book:
    def __init__(self):
        self.title=input("enter title")
        self.author = input("enter author")
        self.price  = int(input("enter price"))
        self.pages = input("enter number of pages")
        self.language = input("enter the language")
    def get_title(self):
        print(self.title)
    def get_author(self):
        print(self.author)
    def get_price(self):
        print(self.price)
    def set_title(self):
        self.title=input('enter new title : ')
        self.get_title()
    def set_author(self):
        self.author=input('enter new author :')
        self.get_author()
    def set_price(self):
        self.price=int(input('enter new price : '))
        self.get_price()
b1=Book()

b1.get_title()
b1.get_author()
b1.get_price()
b1.set_price()
b1.set_title()
b1.set_author()
