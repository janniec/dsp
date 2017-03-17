[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import thinkstats2
import thinkplot

# get data
import first
live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
ages = live.agepreg
weights = live.totalwgt_lb

# make a scatter plot of birth weight versus mother’s age
thinkplot.Scatter(ages, weights, alpha=1, s=10)
thinkplot.Config(xlabel='Age (years)',
                 ylabel='Weight (lbs)',
                 xlim=[10, 45],
                 ylim=[0, 15],
                 legend=False)
# RESULTS: messy plot

# Plot percentiles of birth weight versus mother’s age
bins = np.arange(10, 45, 5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)
# binned mother's age

mean_ages = [group.agepreg.mean() for i, group in groups]
cdfs_wgt= [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weight_percentiles = [cdf.Percentile(percent) for cdf in cdfs_wgt]
    label = '%dth' % percent
    thinkplot.Plot(mean_ages, weight_percentiles, label=label)
# plotting percentiles of baby weight
    
thinkplot.Config(xlabel= "Mother's age (years)",
                 ylabel='Weight (lbs)',
                 xlim=[10, 45], 
                 legend=True)
# RESULTS: plot

# Compute Pearson’s and Spearman’s correlations. 
def Cov(xs, ys, meanx=None, meany=None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov

def Corr(xs, ys): # Pearson's
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / np.sqrt(varx * vary)
    return corr
 
import pandas as pd

def SpearmanCorr(xs, ys):  # Spearmans'
    xranks = pd.Series(xs).rank()
    yranks = pd.Series(ys).rank()
    return Corr(xranks, yranks)

print('Corr', Corr(ages, weights))
print('SpearmanCorr', SpearmanCorr(ages, weights))
# RESULTS: Corr 0.0688339703541
# SpearmanCorr 0.0946100410966

# How would you characterize the relationship between these variables?

# Scatterplot: does not show a relationship between the variables. The mothers' ages
# do not indicate anything about their babies' weights.

# Percentile Plot: The relationship between mother's age and baby's weight are not linear. 
# Between the mother's age range from about 18 to about 27, there appears to be a subtle 
# positive correlation, where baby weight increases as mother's age increases.

# Correlations: Pearson's correlation shows a positive but weak correlations between the 
# variables. Spearman's correlation is higher, likely because of a nonlinear relationship
# between the variables and/or Pearson's correlation is taking into account outliers.  








