#!/usr/bin/python

InFile = open("count.txt", "r")
Hits = InFile.readline()
n = int(Hits) + 1
h = str(n)
InFile.close()
OutFile = open("count.txt", "w")
OutFile.write(h)
OutFile.close

