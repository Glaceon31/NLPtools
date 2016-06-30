#-*- coding: utf-8 -*-
import codecs
import re
import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('filein')
parser.add_argument('fileout')

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
			if word != 'UNK':
				result[num].append(word)
		result[num] = ' '.join(result[num])
		num += 1

	enoutput = codecs.open(args.fileout, 'w', 'utf-8')
	enoutput.write('\n'.join(result))
	enoutput.close()