import codecs
import argparse

parser = argparse.ArgumentParser(description='transform stanford parser output format to niutrans input format')
parser.add_argument('input_file')
parser.add_argument('output_file')

args = parser.parse_args()

content = codecs.open(args.input_file, 'r', 'utf-8').read()
sentences = content.split('\n')[0:-1]
outputsentences = []
print len(sentences), 'lines total'
count = 0
for sentence in sentences:
	outputsentences.append('( '+sentence+')')
output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()