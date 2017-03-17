[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

# imports
from __future__ import print_function, division

%matplotlib inline

import numpy as np

import thinkstats2
import thinkplot

def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.loc[41, 'log_upper'] = log_upper
    
    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample
    
# get data
import hinc
income_df = hinc.ReadData()

log_sample = InterpolateSample(income_df, log_upper=6.0)

log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Config(xlabel='Household income (log $)',
               ylabel='CDF')
# RESULTS: plot

sample = np.power(10, log_sample)

cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Household income ($)',
               ylabel='CDF')
# RESULTS: plot

# Median
def Median(xs):
    cdf = thinkstats2.Cdf(xs)
    return cdf.Value(0.5)

Median(sample)
# RESULTS: 51226.454478940461

# Mean
def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)
# Raw moments are just sums of powers.

def Mean(xs):
    return RawMoment(xs, 1)
# The first raw moment is the mean.
# When k = 1 the result is he sample mean.

Mean(sample)
# RESULTS: 74278.707531187392

# skewness
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)
# The central moments are powers of distances from the mean.
# When k = 2 the result is the variance.

def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = np.sqrt(var)
    return CentralMoment(xs, k) / std**k
# The standardized moments are ratios of central moments, 
# with powers chosen to make the dimensions cancel.

def Skewness(xs):
    return StandardizedMoment(xs, 3)
# The third standardized moment is skewness.

Skewness(sample)
# RESULTS: (4.9499202444295793)

# pearson's skewness
def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    # The second central moment is the variance.

    std = np.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp

PearsonMedianSkewness(sample)
# RESULTS: 0.73612580191417953

# What fraction of households reports a taxable income below the mean?
cdf.Prob(Mean(sample))
# 66% reports a taxable income below the mean
# RESULTS: 0.66000587956687196
