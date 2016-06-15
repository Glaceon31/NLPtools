import codecs
import argparse
import re
import os
import string

parser = argparse.ArgumentParser(description='intergrating aligned corpus texts')
parser.add_argument('source')
parser.add_argument('translate')
parser.add_argument('ref', nargs='+')

args = parser.parse_args()


content=codecs.open(args.source, 'r', 'utf-8').read()
source = content.split('\n')[0:-1]
print len(source)
print len(source[0].split(' '))

content=codecs.open(args.translate, 'r', 'utf-8').read()
translate = content.split('\n')[0:-1]
print len(translate)
assert len(source) == len(translate)

content = []
refs = []
for i in xrange(len(args.ref)):
	content.append(codecs.open(args.ref[i], 'r', 'utf-8').read())
	refs.append(content[i].split('\n')[0:-1])
	assert len(refs[i]) == len(translate)

translatebylength = []
refbylength = []
for i in xrange(200):
	translatebylength.append([])

for i in xrange(len(args.ref)):
	refbylength.append([])
	for j in xrange(200):
		refbylength[i].append([])

for i in xrange(len(translate)):
	length = len(source[i].split(' '))/3
	translatebylength[length].append(translate[i]) 
	for j in xrange(len(args.ref)):
		refbylength[j][length].append(refs[j][i])

xco = []
results = []
for i in xrange(0, 200):
	if len(translatebylength[i]) > 0:
		output = codecs.open('bleubylength/'+str(i)+'.tr', 'w', 'utf-8')
		output.write('\n'.join(translatebylength[i])+'\n')
		output.close()
		cmd = 'perl multi-bleu.perl -lc '
		for j in xrange(len(args.ref)):
			output = codecs.open('bleubylength/'+str(i)+'.en'+str(j), 'w', 'utf-8')
			output.write('\n'.join(refbylength[j][i])+'\n')
			output.close() 
			cmd += 'bleubylength/'+str(i)+'.en'+str(j)+' '
		cmd += ' < '+'bleubylength/'+str(i)+'.tr'
		#print cmd
		a = os.popen(cmd)
		st = a.read()
		result = st[st.find('=')+2:st.find(',')]
		print result
		xco.append(i*3)
		results.append(string.atof(result))
print xco
print results