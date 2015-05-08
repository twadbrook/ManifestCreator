#!/usr/bin/python

import csv
import os

MUNKI_REPO = "/Users/Shared/munki/manifests"

with open('serials.csv', mode='r') as infile:
    reader = csv.reader(infile)
    keyDict = dict(reader)

for key in keyDict.keys():
#	f = open(os.path.join(MUNKI_REPO, str(key)), 'w')
#	f.close()
	print key