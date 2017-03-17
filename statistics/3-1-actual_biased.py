[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

# get data
resp = nsfg.ReadFemResp()

# actual distribution for the number of children under 18 in the respondents' households
actual_pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
actual_pmf
# RESULTS: Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
# biased distribution we would see if we surveyed the children 
# and asked them how many children under 18 (including themselves) are in their household
biased_pmf = BiasPmf(actual_pmf, label='biased')
biased_pmf
# RESULTS: Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})

# Plot the actual and biased distributions
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')
# RESULTS: pretty plot

# compute their means
print('Actual mean', actual_pmf.Mean())
print('Observed mean', biased_pmf.Mean())
# RESULTS: Actual mean 1.02420515504
# Observed mean 2.40367910066
