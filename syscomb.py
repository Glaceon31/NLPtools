import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='build corpus for syscomb')
parser.add_argument('input_file', nargs='+')
parser.add_argument('split_sym')
parser.add_argument('output_file')

args = parser.parse_args()
print args.input_file

content = []
sentences = []
for i in xrange(len(args.input_file)):
	content.append(codecs.open(args.input_file[i], 'r', 'utf-8').read())
	sentences.append(content[i].split('\n')[0:-1])
	print len(sentences[i])
	assert len(sentences[i]) == len(sentences[0])

outputsentences = []
for i in xrange(len(sentences[i])):
	inputs = ''
	for j in xrange(len(args.input_file)):
		inputs += sentences[j][i] + ' '+args.split_sym+' '
	outputsentences.append(inputs)

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()