#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

'''
    Seq2seq attention matrix heatmap 
    Liner Yang
    2016/06/29
'''
# set appropriate font and dpi
sns.set(context="paper", font="monospace")
sns.set(font_scale=1.2)
sns.set_style({"savefig.dpi": 200})

zh = []
en = []

for i, line in enumerate(open('zh')):
    zh.append([w.decode('utf8') for w in line.strip().split()])

for i, line in enumerate(open('en')):
    en.append([w.decode('utf8') for w in line.strip().split()])

t = open('1', 'r').read().replace(')','').replace('array(','').replace(', dtype=float32', '')
p = np.asarray(np.asarray(eval(t)), dtype="float32")
p = p.transpose()
print p.shape
#p = np.genfromtxt('1')

# 
align = pd.DataFrame(p, index=zh, columns=en)

# plot it out
ax = sns.heatmap(align)
# set the x-axis labels on the top
ax.xaxis.tick_top()
# rotate the x-axis labels
plt.xticks(rotation=90)
plt.yticks(rotation=0)
# get figure (usually obtained via "fig,ax=plt.subplots()" with matplotlib)
fig = ax.get_figure()
plt.show()


# specify dimensions and save
# fig.set_size_inches(15, 20)
# fig.savefig("align.pdf", format='pdf')
