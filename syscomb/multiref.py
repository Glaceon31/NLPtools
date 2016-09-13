import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='intergrating aligned corpus texts')
parser.add_argument('input_file', nargs='+')
parser.add_argument('output_file')

args = parser.parse_args()
print args.input_file

content = []
sentences = []
for i in xrange(len(args.input_file)):
	content.append(codecs.open(args.input_file[i], 'r', 'utf-8').read())
	sentences.append(content[i].split('\n')[0:-1])
	assert len(sentences[i]) == len(sentences[0])


outputsentences = []
for i in xrange(len(sentences[i])):	
	for j in xrange(len(args.input_file)):
		outputsentences.append(sentences[j][i])

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()