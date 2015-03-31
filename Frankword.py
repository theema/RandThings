# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:23:11 2015

@author: Theema
Program to count words and find M.S message
"""
text = ""
file = open('Frankenstein.txt')
for line in file:
    text+=line

ignore = ["that","what","with","this","would","from","your","which","while","these","could"]
strip = ['.',',','?',')','(',';',':', '!', '"']
wordsMin = 4

words = text.lower().split()
wordcount = {}
for word in words:
    for symbol in strip:
        if symbol in word:
            word = word.replace(symbol, "")
    if word not in ignore and len(word) > wordsMin:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
  
sort =  sorted(wordcount,key=wordcount.get)
def print_txt(sort):
	for word in sort:
		print (word, wordcount[word])
print_txt(sort)
def print_html(sortedbyfrequency):
	print ("<html><head><title>Wordcount.py Output</title></head><body><table>")
	for word in sortedbyfrequency:
		print ("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
	print ("</table></body></html>")
#print_html(sort)
