#-*- coding: utf-8 -*-
import codecs
import re
import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('filein')
parser.add_argument('fileout')

filt = string.punctuation+'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()+'1234567890'

def iseng(word):
	for i in xrange(len(word)):
		#print word[i]
		if not word[i] in filt:
			return False
	return True

if __name__ == '__main__':
	args = parser.parse_args()
	enfile = codecs.open(args.filein, 'r', 'utf-8')
	en = enfile.read()
	enfile.close()

	sentences = en.split('\n')
	result = []
	num = 0
	for sentence in sentences:
		words = sentence.split(' ')
		#print words
		result.append([])
		for word in words:
			if iseng(word):
				result[num].append(word)
		result[num] = ' '.join(result[num])
		num += 1

	enoutput = codecs.open(args.fileout, 'w', 'utf-8')
	enoutput.write('\n'.join(result))
	enoutput.close()