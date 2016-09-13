import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='build input for unkreplace alignment')
parser.add_argument('source_file')
parser.add_argument('target_file')
parser.add_argument('output_file')

args = parser.parse_args()


a = codecs.open(args.source_file, 'r', 'utf-8').read()
source = a.split('\n')[0:-1]
a = codecs.open(args.target_file, 'r', 'utf-8').read()
target = a.split('\n')[0:-1]
print len(source)
assert len(source) == len(target)

outputsentences = []
for i in xrange(len(source)):
	outputsentences.append(source[i]+' ||| '+ target[i])

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()