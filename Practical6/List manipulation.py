#Store information in separate lists.

gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]


#I want to divide gene_lengths by the corresponding exon_counts, so I want to create ndarray.

import numpy as np
a = np.array(gene_lengths)
b = np.array(exon_counts)

#Calculate the average exon lengths.

c = a/b


#Draw a boxplot.

import matplotlib.pyplot as plt


#There are 10 elements in this boxplot.

n = 10
score = c


#What information I want this boxplot to show?

plt.boxplot(score,

            #If the boxplot is vertical?
            vert = True,

            #Decide the interquartile range.
            whis = 1.5,

            #If the box is colored?
            patch_artist = False,

            #Can we see the mean value in the boxplot?
            meanline = False,

            #Can we see the box?
            showbox = True,

            #Can we see the minimum and maximum?
            showcaps = True,

            #Can we see outliers?
            showfliers = True,

            #If there is notch?
            notch = False
              )

#Show the boxplot.

plt.show()
