# -*- coding: utf-8 -*-
import re, codecs, os

y2n = {"<10":0, "<20":0, "<30":0, "<40":0, "<50":0, "<60":0, "<70":0, "<80":0, "<90":0, "<100":0}
for line in codecs.open("test.txt",'r','utf-8'):
	if not line.strip():
		continue
	y = ""
	if re.match("(\d+)", line.strip()):
		y = re.match("(\d+)", line.strip()).group(1)
	else:
		print(line)
	y = int(y)
	if re.search("月|周|天", line.strip()):
		y = 1
	if y < 10:
		y2n["<10"] += 1
	elif y< 20:
		y2n["<20"] += 1
	elif y< 30:
		y2n["<30"] += 1
	elif y< 40:
		y2n["<40"] += 1
	elif y< 50:
		y2n["<50"] += 1
	elif y< 60:
		y2n["<60"] += 1
	elif y< 70:
		y2n["<70"] += 1
	elif y< 80:
		y2n["<80"] += 1
	elif y< 90:
		y2n["<90"] += 1
	else:
		print(line)
		os._exit(0)

print(y2n)