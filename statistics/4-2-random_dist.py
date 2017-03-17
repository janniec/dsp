[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

# Generate 1000 numbers from numpy.random.random 
thousand = np.random.random(1000)

# plot their PMF. 
pmf = thinkstats2.Pmf(thousand)
thinkplot.Pmf(pmf, linewidth= 0.1)
thinkplot.Config(xlabel='Random Values', ylabel='PMF')
# What goes wrong?
# Because the numbers generated are uniform between 0 to 1, 
# the random values all have the same frequnecy and therefore the same probability. 
# the plot shows that every value has 0.0010 probability.
# RESULT: barcode-looking plot

# Now plot the CDF. 
cdf = thinkstats2.Cdf(thousand)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random Values', ylabel='CDF', loc='upper left')
# Is the distribution uniform? Yes.
# RESULT: rough diagnal line plot
