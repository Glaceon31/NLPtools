import codecs
import re
import argparse

parser = argparse.ArgumentParser(description='transform phrase structure to tokenized sentences')
parser.add_argument('input_file')
parser.add_argument('output_file')

args = parser.parse_args()

content = codecs.open(args.input_file, 'r', 'utf-8').read()
sentences = content.split('\n')[0:-1]
outputsentences = []
print len(sentences), 'lines total'
count = 0
for sentence in sentences:
	words = []
	left = False
	lastleft = -1
	for i in xrange(len(sentence)):
		if sentence[i] == '(':
			lastleft = i
			left = True
		if left and sentence[i] == ')':
			words.append(sentence[lastleft+1:i].split(' ')[1])
			left = False
	outputsentence = ' '.join(words)
	outputsentences.append(outputsentence)
	count += 1
	if count % 10000 == 0:
		print count, 'lines processed'
output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()
