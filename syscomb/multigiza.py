import sys
import codecs

num_system = len(sys.argv)-2

content = []
sentences = []
for i in xrange(num_system):
	content.append(codecs.open(sys.argv[i+1], 'r', 'utf-8').read())
	sentences.append(content[i].split('\n')[0:-1])
	assert len(sentences[i]) == len(sentences[0])

num_sentences = len(sentences[0])
output_a = []
output_b = []
for i in range(num_sentences):
	for j in range(num_system):
		for k in range(num_system):
			if j == k:
				continue
			output_a.append(sentences[j][i])
			output_b.append(sentences[k][i])

output = codecs.open(sys.argv[-1]+'.a', 'w', 'utf-8')
output.write('\n'.join(output_a)+'\n')
output.close()
output = codecs.open(sys.argv[-1]+'.b', 'w', 'utf-8')
output.write('\n'.join(output_b)+'\n')
output.close()