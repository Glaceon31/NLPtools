import codecs
import argparse

parser = argparse.ArgumentParser(description='build dev set format file for niutrans tree2string translator')
parser.add_argument('input_src_file', help='source tokenized sentences')
parser.add_argument('input_trg_file_0', help='target tokenized sentences 0')
parser.add_argument('input_trg_file_1', help='target tokenized sentences 1')
parser.add_argument('input_trg_file_2', help='target tokenized sentences 2')
parser.add_argument('input_trg_file_3', help='target tokenized sentences 3')
parser.add_argument('output_file')

args = parser.parse_args()

content_srctok = codecs.open(args.input_src_tok_file, 'r', 'utf-8').read()
content_trgtok0 = codecs.open(args.input_trg_tok_file_0, 'r', 'utf-8').read()
content_trgtok1 = codecs.open(args.input_trg_tok_file_1, 'r', 'utf-8').read()
content_trgtok2 = codecs.open(args.input_trg_tok_file_2, 'r', 'utf-8').read()
content_trgtok3 = codecs.open(args.input_trg_tok_file_3, 'r', 'utf-8').read()

sentences_srctok = content_srctok.split('\n')[0:-1]
sentences_trgtok0 = content_trgtok0.split('\n')[0:-1]
sentences_trgtok1 = content_trgtok1.split('\n')[0:-1]
sentences_trgtok2 = content_trgtok2.split('\n')[0:-1]
sentences_trgtok3 = content_trgtok3.split('\n')[0:-1]

print len(sentences_srctok),'lines totoal'

outputsentences = []

for sentence_srctok, sentence_trgtok0, sentence_trgtok1, sentence_trgtok2, sentence_trgtok3 in zip(sentences_srctok, sentences_trgtok0, sentences_trgtok1, sentences_trgtok2, sentences_trgtok3):
	outputsentences.append(sentence_srctok+'\n\n'+sentence_trgtok0+sentence_trgtok1+sentence_trgtok2+sentence_trgtok3)

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()