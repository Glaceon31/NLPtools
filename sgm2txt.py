import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='remove all spaces')
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('ref_num', type=int, default=1)

args = parser.parse_args()

ref_num = args.ref_num
content = codecs.open(args.input_file, 'r', 'utf-8').read()

segre = re.compile('> (.*?)</seg>')
sentences = segre.findall(content)

print len(sentences)

if ref_num == 1:
	output = codecs.open(args.output_file, 'w', 'utf-8')
	output.write('\n'.join(sentences)+'\n')
	output.close()
else:
	for i in xrange(ref_num):
		output = codecs.open(args.output_file+str(i), 'w', 'utf-8')
		output.write('\n'.join(sentences[i*len(sentences)/ref_num:(i+1)*len(sentences)/ref_num])+'\n')
		output.close()