#!/usr/bin/python

import csv
import os

MUNKI_REPO = "/Users/Shared/munki/manifests"

with open('/Library/Server/Web/Data/Sites/Default/serials.csv', mode='r') as infile:
    reader = csv.reader(infile)
    keyDict = dict(reader)

for items in keyDict.values():
	f = open(os.path.join(MUNKI_REPO, str(items)), 'w')
	f.close()
#	print items