import codecs
import argparse
import re

parser = argparse.ArgumentParser(description='generate a text with n lines of "FAIL"')
parser.add_argument('num', type=int)
parser.add_argument('output_file')

args = parser.parse_args()


content = 'FAIL\n'*args.num

output = codecs.open(args.output_file, 'w', 'utf-8')
output.write(content)
output.close()