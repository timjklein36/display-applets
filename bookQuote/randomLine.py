#!/bin/env python3
# ----------------------------------------------------------
# RandomLine
#-----------------------------------------------------------

from random import randint

def sentences(book):
	return book.split(".")

def randel(list):
	return list[randint(0, len(list))]

def escape(s):
	return s.replace("Mrs.", "Mrs@").replace("Dr.", "Dr@").replace("Mr.", "Mr@")

def unescape(s):
	return s.replace("Mrs@", "Mrs.").replace("Dr@", "Dr.").replace("Mr@", "Mr.").replace("\n", " ")

def linefrom(bookfile):
	with open(bookfile, "r") as fp:
		book = fp.read()
		return unescape(randel(sentences(escape(book)))) + "."

for i in range(15):
	print("> ", linefrom("two cities.txt"))
	print()

