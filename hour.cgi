#!/usr/bin/python

InFile = open("timesheet.txt", "r")
#Hits = InFile.readline()
x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in InFile:
	n = int(i)
	x[n] = x[n] + 1
InFile.close()
print "<p><h3>Number of visits per hour (0 - 23): </h3><br>"
print x

