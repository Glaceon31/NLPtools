import codecs
import argparse

parser = argparse.ArgumentParser(description='build dev set format file for niutrans tree2string translator')
parser.add_argument('input_src_tok_file', help='source tokenized sentences')
parser.add_argument('input_tree_file', help='phrase structure trees')
parser.add_argument('input_trg_tok_file', help='target tokenized sentences')
parser.add_argument('output_file')

args = parser.parse_args()

content_srctok = codecs.open(args.input_src_tok_file, 'r', 'utf-8').read()
content_tree = codecs.open(args.input_tree_file, 'r', 'utf-8').read()
content_trgtok = codecs.open(args.input_trg_tok_file, 'r', 'utf-8').read()

sentences_srctok = content_srctok.split('\n')[0:-1]
sentences_tree = content_tree.split('\n')[0:-1]
sentences_trgtok = content_trgtok.split('\n')[0:-1]

assert len(sentences_srctok) == len(sentences_tree)
assert len(sentences_srctok) == len(sentences_trgtok)
print len(sentences_srctok), 'lines total'

outputsentences = []

for sentence_srctok, sentence_tree, sentence_trgtok in zip(sentences_srctok,sentences_tree, sentences_trgtok):
	outputsentences.append(sentence_srctok+' ||||  |||| '+sentence_tree)
	outputsentences.append(sentence_tree)
	outputsentences.append(sentence_trgtok)


output = codecs.open(args.output_file, 'w', 'utf-8')
output.write('\n'.join(outputsentences)+'\n')
output.close()