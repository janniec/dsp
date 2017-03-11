# Part I - Regular Expressions

# Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
import pandas as pd
import numpy as np
from pprint import pprint
import csv
import ast

url = "https://raw.githubusercontent.com/thisismetis/dsp/master/python/faculty.csv"
df = pd.read_csv(url)

# What am I working with?
df.info()
# Need to clean up column titles
df = df.rename(columns={' degree': 'degree'})
df = df.rename(columns={' title': 'title'})
df = df.rename(columns={' email': 'email'})
df.info()

# What needs to be fixed?
df['degree'].unique()
# need to clean up the 'degree' data
df['degree'] = df['degree'].str.replace('.', '') # remove the periods
#strip unnecessary first space
df['degree'] = df['degree'].map(lambda x: x.strip())

# Create dummy variables to figure out frequency
deg_copy = df.copy()
dum_degree = pd.concat([deg_copy, df['degree'].str.get_dummies(sep=' ')], axis=1)

# Get frequency of each dummy variable
dum_degree.ix[:, 4:].sum()
# ANSWER:
# 0        1
# BSEd     1
# JD       1
# MA       1
# MD       1
# MPH      2
# MS       2
# PhD     31
# ScD      6
# dtype: int64




# Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
# What am I working with?
df['title'].unique()
# Clean up 'title data.
df['title'] = df['title'].str.replace(' is ', ' of ') # correct the title
df['title'] = df['title'].str.replace(' of Biostatistics', '')

# Create dummy variables
tit_copy = df.copy()
tit_dum = pd.get_dummies(df.title)
dum_title = pd.concat([tit_copy, tit_dum], axis=1)

# Get frequencies
dum_title.ix[:, 4:].sum()
# ANSWER:
# Assistant Professor    12
# Associate Professor    12
# Professor              13
# dtype: int64






# Q3. Search for email addresses and put them in a list. Print the list of email addresses.
print df['email'].tolist()
# ANSWER:
# ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu',
#'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu',
#'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu',
#'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu',
#'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu',
#'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu',
#'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu',
#'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu',
#'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu',
#'weiyang@mail.med.upenn.edu']


# Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).
#Print the list of unique email domains.
# Split domain from emails
domain = df['email'].map(lambda x: x.split('@')[1])
# Verify that I got all the unique domains
domain.unique()
# number of unique domains
domain.nunique()
# ANSWER: 4
