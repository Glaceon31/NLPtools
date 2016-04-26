import codecs
import argparse

parser = argparse.ArgumentParser(description='build dev set format file for niutrans tree2string translator')
parser.add_argument('input_src_file', help='source tokenized sentences')
parser.add_argument('input_trg_file', help='target tokenized sentences files', nargs='+')
parser.add_argument('output_file')

args = parser.parse_args()

print args.input_trg_file
content_srctok = codecs.open(args.input_src_file, 'r', 'utf-8').read()
content_trgtok = []
for i in xrange(len(args.input_trg_file)):
	content_trgtok.append(codecs.open(args.input_trg_file[i], 'r', 'utf-8').read())

sentences_srctok = content_srctok.split('\n')[0:-1]
sentences_trgtok = []
for i in xrange(len(args.input_trg_file)):
	sentences_trgtok.append(content_trgtok[i].split('\n')[0:-1])
	assert len(sentences_srctok) == len(sentences_trgtok[i])
print len(sentences_srctok),'lines totoal'

outputsentences = []

for i in xrange(len(sentences_srctok)):
	outputsentences.append(sentences_srctok[i]+'\n')
	for j in xrange(len(args.input_trg_file)):
		outputsentences.append(sentences_trgtok[j][i])

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()