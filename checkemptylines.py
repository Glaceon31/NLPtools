import codecs
import string
import sys

aligns = open(sys.argv[1], 'r').read().split('\n')[:-1]

print 'total:',len(aligns)
for i in xrange(len(aligns)):
	if aligns[i].replace(' ','') == '':
		print i