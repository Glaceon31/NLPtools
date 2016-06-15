import codecs
import argparse
import re
import os
import string

parser = argparse.ArgumentParser(description='calculate BLEU for each sentence')
parser.add_argument('--translate', nargs='+')
parser.add_argument('--ref', nargs='+')

args = parser.parse_args()

print args.translate
print args.ref

content = []
trans = []
for i in xrange(len(args.translate)):
	content.append(codecs.open(args.translate[i], 'r', 'utf-8').read())
	trans.append(content[i].split('\n')[0:-1])
	assert len(trans[i]) == len(trans[0])

content = []
refs = []
for i in xrange(len(args.ref)):
	content.append(codecs.open(args.ref[i], 'r', 'utf-8').read())
	refs.append(content[i].split('\n')[0:-1])
	assert len(refs[i]) == len(trans[0])

try:
	os.mkdir('bleubysentence')
except:
	pass
print len(trans[0])
best = 0
bestmiddle = 0
worst = 0
worstmiddle = 0
middle = 0
for i in xrange(len(trans[0])):
	cmd = 'perl multi-bleu.perl -lc '
	for j in xrange(len(args.ref)):
		output = codecs.open('bleubysentence/'+str(i)+'_'+str(j)+'.ref', 'w', 'utf-8')
		output.write(refs[j][i]+'\n')
		output.close()
		cmd += 'bleubysentence/'+str(i)+'_'+str(j)+'.ref '
	results = []
	for j in xrange(len(args.translate)):
		output = codecs.open('bleubysentence/'+str(i)+'_'+str(j)+'.tr', 'w', 'utf-8')
		output.write(trans[j][i]+'\n')
		output.close()
		a = os.popen(cmd+' < '+'bleubysentence/'+str(i)+'_'+str(j)+'.tr')
		st = a.read()
		result = st[st.find('=')+2:st.find(',')]
		print result,
		results.append(string.atof(result))
	print 
	if results[-1] > max(results[0:-1]):
		best += 1
	elif results[-1] == max(results[0:-1]):
		bestmiddle += 1
	elif results[-1] < max(results[0:-1]) and results[-1] > min(results[0:-1]):
		middle += 1
	elif results[-1] == min(results[0:-1]):
		worstmiddle += 1
	elif results[-1] < min(results[0:-1]):
		worst += 1

print worst, worstmiddle, middle, bestmiddle, best

	

exit()
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