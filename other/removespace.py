import codecs
import argparse

parser = argparse.ArgumentParser(description='remove all spaces')
parser.add_argument('input_file')
parser.add_argument('output_file')

args = parser.parse_args()

content = codecs.open(args.input_file, 'r', 'utf-8').read()
det = content.replace(' ','')
output = codecs.open(args.output_file, 'w', 'utf-8')
output.write(det)
output.close()