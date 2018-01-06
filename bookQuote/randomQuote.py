#!/bin/env python3
# ----------------------------------------------------------
# RandomQuote
#-----------------------------------------------------------

from random import randint
import re

def quotes(book):
	return re.split(r'[ ](?=\"[^"]*\"[^.]*\.)', book)

def randel(list):
	return list[randint(0, len(list))]

def escape(s):
	return s.replace("Mrs.", "Mrs@").replace("Dr.", "Dr@").replace("Mr.", "Mr@")

def unescape(s):
	return s.replace("Mrs@", "Mrs.").replace("Dr@", "Dr.").replace("Mr@", "Mr.").replace("\n", " ")

def quotefrom(bookfile):
	with open(bookfile, "r") as fp:
		book = fp.read()
		quoteBlock = unescape(randel(quotes(escape(book))))
		match = re.match(r'\"[^"]*\"[^.]*\.', quoteBlock)
		if match:
			return match[0]
		else:
			return '!!!!!!'

for i in range(15):
	print("> ", quotefrom("mortal coils.txt"))
	print()

