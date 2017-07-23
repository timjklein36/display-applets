#!/bin/env python3
# ----------------------------------------------------------
# RandomQuote
#-----------------------------------------------------------

from random import randint

def sentences(book):
    return book.split(".")

def randel(list):
    return list[randint(0, len(list))]

def escape(s):
    def foo(y):
        print(s)
        print(y)

    return s.replace("Mrs.", "Mrs@").replace("Dr.", "Dr@").replace("Mr.", "Mr@")

def unescape(s):
    return s.replace("Mrs@", "Mrs.").replace("Dr@", "Dr.").replace("Mr@", "Mr.").replace("\n", " ")

def quotefrom(bookfile):
    with open(bookfile, "r") as fp:
        return unescape(randel(sentences(escape(fp.read())))) + "."

def addints(x, y):
    return x + y

def mydivide(x, y):
    return x / y

for i in range(15):
    print("> ", quotefrom("dracula.txt"))
    print()

