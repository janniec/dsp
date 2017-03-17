[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

# imports
from __future__ import print_function, division
%matplotlib inline
import numpy as np
import random

import thinkstats2
import thinkplot

class HypothesisTest(object):

    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)

    def PValue(self, iters=1000):
        self.test_stats = [self.TestStatistic(self.RunModel()) 
                           for _ in range(iters)]

        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count / iters

    def TestStatistic(self, data):
        raise UnimplementedMethodException()

    def MakeModel(self):
        pass

    def RunModel(self):
        raise UnimplementedMethodException()

class DiffMeansPermute(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self): # combines the groups into one
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self): # permutation
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data

# Write a class named DiffMeansResample that inherits from DiffMeansPermute and 
# overrides RunModel to implement resampling, rather than permutation.

class DiffMeansResample(DiffMeansPermute):
    """Tests a difference in means using resampling."""
    
    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        #def Resample(xs):
        #    return np.sample.choice(xs, len(xs), replace=True)
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        # we still pool the groups? Is that ok because we didn't suffle?
        return group1, group2
 
# get info
import first
live, firsts, others = first.MakeFrames()

# Use this model to test the differences in pregnancy length and birth weight. 
def RunResampleTest(firsts, others):
    """Tests differences in means by resampling.

    firsts: DataFrame
    others: DataFrame
    """
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\ndiff means resample preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = DiffMeansPermute(data)
    p_value = ht.PValue(iters=10000)
    print('\ndiff means resample birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

RunResampleTest(firsts, others)
# comparing results with pvalues from previous exercise 9.1: 

# test1: difference in mean pregnancy length (Using Perumtation Test)
# test2: difference in mean birth weight (Using Perumtation Test)
# test3: correlation of mother's age and birth weight
# test4: chi-square test of pregnancy length

# n       test1   test2   test3   test4
# 9148	0.17	0.00	0.00	0.00
# 4574	0.09	0.06	0.00	0.00
# 2287	0.93	0.00	0.00	0.00
# 1143	0.35	0.82	0.03	0.00
# 571	0.11	0.41	0.47	0.00
# 285	0.32	0.76	0.55	0.23
# 142	0.13	0.55	0.52	0.04


# Conclusion: As expected, tests that are positive with large sample
# sizes become negative as we take away data.  But the pattern is
# erratic, with some positive tests even at small sample sizes.

# RESULTS: diff means resample preglength
# p-value = 0.1699
# actual = 0.0780372667775
# ts max = 0.228461172723

# diff means resample birthweight
# p-value = 0.0001
# actual = 0.124761184535
# ts max = 0.125592004226

# How much does the model affect the results?

# Comparing the results: 
# Permutation Test on pregnancy length with a sample of 9148, Pvalue is: 0.17
# Resampling Test on pregancy lenght with a sample of 10000, Pvalue is: 0.1699
# Permutation Test on birth weight with a sample of 9148, Pvalue is: 0.00
# Resampling Test on birth weight with a sample of 10000, Pvalue is: 0.0001

# Using different tests doesn't appear to affect the results much. 
# For both tests, the null hyptheses are (A) likelihood of finding the result 
# that first pregnancies being longer assuming there is no difference 
# between first babies and other babies; and (B) likelihood of finding the result 
# that first babies are lighter than other babies assuming there is no difference
# between first pregnancies and other pregnancies. 

# The permutation test creates this assumption of no difference, through shuffling the data.
# The resampling test creates this assumpition through drawing samples from the pool 
# with replacments. These to methods do not appear to create a measurable difference 
# in the assumption.  

