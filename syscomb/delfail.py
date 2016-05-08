import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='delete "FAIL"s and corrsponding sentences in all files')
parser.add_argument('input_file', nargs='+')

args = parser.parse_args()
print args.input_file

content = []
sentences = []
outputsentences = []
for i in xrange(len(args.input_file)):
	content.append(codecs.open(args.input_file[i], 'r', 'utf-8').read().replace('\r',''))
	sentences.append(content[i].split('\n')[0:-1])
	print len(sentences[i])
	assert len(sentences[i]) == len(sentences[0])
	outputsentences.append([])

print sentences
for i in xrange(len(sentences[i])):
	nofail = True
	for j in xrange(len(args.input_file)):
		if sentences[j][i] == 'FAIL':
			nofail = False
	if nofail:
		for j in xrange(len(args.input_file)):
			outputsentences[j].append(sentences[j][i])

print len(outputsentences[0])
for i in xrange(len(args.input_file)):
	output = codecs.open(args.input_file[i]+'_delfail', 'w', 'utf-8')
	output.write('\n'.join(outputsentences[i])+'\n')
	output.close()
