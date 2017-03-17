[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import thinkstats2
import thinkplot

# a sample with size n=10 from an 
# exponential distribution with λ=2. 
# Simulate this experiment 1000 times

def Estimate3(j):
    n = j
    m=1000
    lam = 2 # paramater determines the shape of the distribution

    estimates = [] # L is an estimator of lambda
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        estimates.append(L)
    return estimates
  
estimates = Estimate3(10)

# Compute the standard error of the estimate 
def RMSE(estimates):
    lam = 2
    """Computes the root mean squared error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float RMSE
    """
    e2 = [(estimate-lam)**2 for estimate in estimates]
    mse = np.mean(e2)
    return np.sqrt(mse)

RMSE(estimates)
# the standard error of estimates: 
# RESULTS: 0.82575542568620752

# the 90% confidence interval.
cdf = thinkstats2.Cdf(estimates)
ci = cdf.Percentile(5), cdf.Percentile(95)
ci
# RESULTS: (1.2461891730043873, 3.7709252739740338)

# plot the sampling distribution of the estimate L. 
def VertLine(x, y=1):
    thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

VertLine(ci[0])
VertLine(ci[1])

thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Estimates',
                 ylabel='CDF',
                 title = 'Sampling Distirbution of estimate L')
# RESULT: pretty plot

# Repeat the experiment with a few different values of n 
# and make a plot of standard error versus n.

def repeat(k):
    estimates = Estimate3(k)
    err = RMSE(estimates)
    print ('RMES = ', err)
    
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('CI = ', ci)
    
    VertLine(ci[0])
    VertLine(ci[1])
    
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='Estimates',
                     ylabel='CDF',
                     title = 'Sampling Distirbution of estimate L')
 
repeat(10)
# RESULTS: RMES =  0.836262929768
# CI =  (1.23203294023293, 3.6931842781755173)
# pretty plot

repeat(100)
# RMES =  0.217125635593
# CI =  (1.6994788041672113, 2.398695140080628)
# pretty plot

repeat(1000)
# RESULT: RMES =  0.0626900049151
# CI =  (1.9004019103156695, 2.1079109440673158)
