#!/usr/bin/python

InFile = open("count.txt", "r")
Hits = InFile.readline()
h = str(int(Hits))
InFile.close()
print "<p><h2>Number of visitors: </h2>" + h + "<br><br>"

