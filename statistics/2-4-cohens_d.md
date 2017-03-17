[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> # import
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import nsfg
import first
import thinkstats2

# get data
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Using the variable totalwgt_lb, 
# investigate whether first babies are lighter or heavier than others.
firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()
# first born babies are lighter on average than others.
# RESULTS: (7.201094430437772, 7.325855614973262)

# Compute Cohen’s effect size to quantify the difference between the groups. 

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d
# Cohen's effect compares the difference between groups the variabilities within groups

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
# Cohen's d for weight difference between first born babies and others.
# RESULTS: -0.088672927072602006

firsts.prglngth.mean(), others.prglngth.mean()
# first born babies have longer pregnancies on average than others.
# RESULTS: (38.60095173351461, 38.52291446673706)

# How does it compare to the difference in pregnancy length?
CohenEffectSize(firsts.prglngth, others.prglngth)
# A comparison of Cohen's d for weight and pregnancy length reveals
# that first born babies tend to have longer pregnancies but lighter weights than others. 
# the effect size for babies' weights is also larger than the effect size for pregnancy length.
# RESULTS: 0.028879044654449883


