[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import nsfg
import first
import analytic
import thinkstats2
import thinkplot

# scipy.stats contains objects that represent analytic distributions
import scipy.stats

# For example scipy.stats.norm represents a normal distribution.
mu = 178 # mean
sigma = 7.7 # standard deviation 
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
# RESULTS: scipy.stats._distn_infrastructure.rv_frozen

# A "frozen random variable" can compute its mean and standard deviation.
dist.mean(), dist.std()
# RESULTS: (178.0, 7.7000000000000002)

# It can also evaluate its CDF. 
# How many people are more than one standard deviation below the mean? About 16%
dist.cdf(mu-sigma)
# RESULTS: 0.15865525393145741

def EvalNormalCdf(x, mu=178, sigma=7.7):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)
    
# How many people are between 5'10" and 6'1"?
min_ht = EvalNormalCdf(177.8)
min_ht
# RESULTS: 0.48963902786483265

max_ht = EvalNormalCdf(185.4)
max_ht
# RESULTS: 0.83173371081078573

# What percentage of the U.S. male population is in this range?
(max_ht - min_ht) * 100
# RESULTS: 34.209468294595311
