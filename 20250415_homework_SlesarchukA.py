import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load penguins dataset
penguins = sns.load_dataset('penguins')
print(penguins.head())

print(penguins['species'].value_counts())

#plot bill depth, mm
sns.boxplot(data = penguins, x='species', y='bill_depth_mm', color='mediumaquamarine', width=0.5)
plt.title('Bill depth grouped by species')
plt.ylabel('Bill length, mm')

#calculate p-values, H0:distributions are the same
peng_adelie = penguins[penguins['species'] == 'Adelie'].dropna()
peng_gentoo = penguins[penguins['species'] == 'Gentoo'].dropna()
peng_chinstrap = penguins[penguins['species'] == 'Chinstrap'].dropna()

from scipy.stats import ranksums
pvals = [ranksums(peng_adelie['bill_depth_mm'], peng_gentoo['bill_depth_mm']).pvalue,
         ranksums(peng_adelie['bill_depth_mm'], peng_chinstrap['bill_depth_mm']).pvalue,
         ranksums(peng_chinstrap['bill_depth_mm'], peng_gentoo['bill_depth_mm']).pvalue
         ]
print(pvals)

#add significance as stars - found a cool package https://starbars.readthedocs.io/en/latest/
import starbars
categories = ['Adelie', 'Gentoo', 'Chinstrap']
annotations = [('Adelie', 'Gentoo', pvals[0]), 
               ('Adelie', 'Chinstrap', pvals[1]),
               ('Gentoo', 'Chinstrap', pvals[2])
               ]

starbars.draw_annotation(annotations)
plt.show()