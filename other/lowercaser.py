#-*- coding: utf-8 -*-
import codecs
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filein')
parser.add_argument('fileout')

if __name__ == '__main__':
	args = parser.parse_args()
	enfile = codecs.open(args.filein, 'r', 'utf-8')
	en = enfile.read()
	enfile.close()
	en = en.lower()
	enoutput = codecs.open(args.fileout, 'w', 'utf-8')
	enoutput.write(en)
	enoutput.close()
	
