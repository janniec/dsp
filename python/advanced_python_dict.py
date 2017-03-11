# Part III - Dictionary

# Q6. Create a dictionary in the below format:
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# Print the first 3 key and value pairs of the dictionary:

# imports
import pandas as pd
import numpy as np
from pprint import pprint
import csv
import ast

# get data into frame
url = "https://raw.githubusercontent.com/thisismetis/dsp/master/python/faculty.csv"
df = pd.read_csv(url)

# Need to clean up column titles
df = df.rename(columns={' degree': 'degree'})
df = df.rename(columns={' title': 'title'})
df = df.rename(columns={' email': 'email'})
df.info()

# Splitting last name from 'name'
df['last_name'] = df.name.str.split('\s+').str[-1]

# Combine 'degree', 'title', and 'emails'
dte_df = df[['degree', 'title', 'email']].copy()
dte_df.update("'" + df[['degree', 'title', 'email']] + "'") # within quotes
dte_df['dte'] = dte_df.apply(lambda row: ', '.join(map(str, row)), axis=1)

# New data frame of just new last name and new combined columns
facu_df = pd.concat([df['last_name'], dte_df['dte']], axis=1)
facu_df.update("[" + facu_df['dte'].astype(object) + "]")

# Turn new dataframe into dictionary
faculty_dict = dict(facu_df.groupby('last_name')['dte'].apply(list))
# URGHHHH. could not figure out how to get rid of the outer double quotes

# Only take the first 3 pairs
faculty3pairs = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
faculty3pairs
# ANSWER:
# {'Bilker': ["['PhD', 'Professor', 'warren@upenn.edu']"],
# 'Feng': ["['PhD', 'Assistant Professor', 'ruifeng@upenn.edu']"],
# 'Putt': ["['PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu']"]}







# Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
#('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
#('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
#('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
#('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
# Print the first 3 key and value pairs of the dictionary:

# Split first name from 'name'
df['first_name'] = df.name.str.split('\s+').str[0]

# Combine ('first', 'last') column
fl_df = df[['first_name', 'last_name']].copy()
fl_df.update("'" + fl_df[['first_name', 'last_name']] + "'")
fl_df['first_last'] = fl_df.apply(lambda row: ', '.join(map(str, row)), axis=1)

# Create new dataframe of just new first name last name column and combined column
prof_df = pd.concat([fl_df['first_last'], dte_df['dte']], axis=1)
prof_df.update("(" + prof_df['first_last'].astype(str) + ")")

# Turn new dataframe into a dictionary
professor_dict = prof_df.set_index('first_last').T.to_dict('list')
professor_dict
# URRRGHHH. Still can't get rid of those darn double quotes

# Only print the first 3 pairs of dictionary:
professor3pairs = {k: professor_dict[k] for k in sorted(professor_dict.keys())[:3]}
professor3pairs
# ANSWER:
# {"('A.', 'Localio')": ["'JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu'"],
# "('Alisa', 'Stephens')": ["'PhD', 'Assistant Professor', 'alisaste@mail.med.upenn.edu'"],
# "('Andrea', 'Troxel')": ["'ScD', 'Professor', 'atroxel@mail.med.upenn.edu'"]}






# Q8. It looks like the current dictionary is printing by first name.
# Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
pprint(sorted(professor_dict.items(),
              key=lambda x: str(x[0].split(" ")[1])))
# UGGH Darn double quotes.
# ANSWER:
# [("('Scarlett', 'Bellamy')",
# ["'ScD', 'Associate Professor', 'bellamys@mail.med.upenn.edu'"]),
# ("('Warren', 'Bilker')", ["'PhD', 'Professor', 'warren@upenn.edu'"]),
# ("('Matthew', 'Bryan')",
#  ["'PhD', 'Assistant Professor', 'bryanma@upenn.edu'"]),
# ("('Jinbo', 'Chen')", ["'PhD', 'Associate Professor', 'jinboche@upenn.edu'"]),
# ("('Jonas', 'Ellenberg')",
#  ["'PhD', 'Professor', 'jellenbe@mail.med.upenn.edu'"]),
# ("('Susan', 'Ellenberg')", ["'PhD', 'Professor', 'sellenbe@upenn.edu'"]),
# ("('Rui', 'Feng')", ["'PhD', 'Assistant Professor', 'ruifeng@upenn.edu'"]),
# ("('Benjamin', 'French')",
#  ["'PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu'"]),
# ("('Phyllis', 'Gimotty')", ["'PhD', 'Professor', 'pgimotty@upenn.edu'"]),
# ("('Wensheng', 'Guo')", ["'PhD', 'Professor', 'wguo@mail.med.upenn.edu'"]),
# ("('Yenchih', 'Hsu')",
#  ["'PhD', 'Assistant Professor', 'hsu9@mail.med.upenn.edu'"]),
# ("('Rebecca', 'Hubbard')",
#  ["'PhD', 'Associate Professor', 'rhubb@mail.med.upenn.edu'"]),
# ("('Wei-Ting', 'Hwang')",
#  ["'PhD', 'Associate Professor', 'whwang@mail.med.upenn.edu'"]),
# ("('Marshall', 'Joffe')",
#  ["'MD MPH PhD', 'Professor', 'mjoffe@mail.med.upenn.edu'"]),
# ("('J.', 'Landis')",
#  ["'BSEd MS PhD', 'Professor', 'jrlandis@mail.med.upenn.edu'"]),
# ("('Hongzhe', 'Li')", ["'PhD', 'Professor', 'hongzhe@upenn.edu'"]),
# ("('Mingyao', 'Li')",
#  ["'PhD', 'Associate Professor', 'mingyao@mail.med.upenn.edu'"]),
# ("('Yimei', 'Li')", ["'PhD', 'Assistant Professor', 'liy3@email.chop.edu'"]),
# ("('A.', 'Localio')",
#  ["'JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu'"]),
# ("('Nandita', 'Mitra')",
#  ["'PhD', 'Associate Professor', 'nanditam@mail.med.upenn.edu'"]),
# ("('Knashawn', 'Morales')",
#  ["'ScD', 'Associate Professor', 'knashawn@mail.med.upenn.edu'"]),
# ("('Kathleen', 'Propert')",
#  ["'ScD', 'Professor', 'propert@mail.med.upenn.edu'"]),
# ("('Mary', 'Putt')", ["'PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu'"]),
# ("('Sarah', 'Ratcliffe')",
#  ["'PhD', 'Associate Professor', 'sratclif@upenn.edu'"]),
# ("('Michelle', 'Ross')",
#  ["'PhD', 'Assistant Professor', 'michross@upenn.edu'"]),
# ("('Jason', 'Roy')",
#  ["'PhD', 'Associate Professor', 'jaroy@mail.med.upenn.edu'"]),
# ("('Mary', 'Sammel')", ["'ScD', 'Professor', 'msammel@cceb.med.upenn.edu'"]),
# ("('Pamela', 'Shaw')", ["'PhD', 'Assistant Professor', 'shawp@upenn.edu'"]),
# ("('Russell', 'Shinohara')",
#  ["'0', 'Assistant Professor', 'rshi@mail.med.upenn.edu'"]),
# ("('Haochang', 'Shou')",
#  ["'PhD', 'Assistant Professor', 'hshou@mail.med.upenn.edu'"]),
# ("('Justine', 'Shults')",
#  ["'PhD', 'Professor', 'jshults@mail.med.upenn.edu'"]),
# ("('Alisa', 'Stephens')",
#  ["'PhD', 'Assistant Professor', 'alisaste@mail.med.upenn.edu'"]),
# ("('Andrea', 'Troxel')",
#  ["'ScD', 'Professor', 'atroxel@mail.med.upenn.edu'"]),
# ("('Rui', 'Xiao')",
#  ["'PhD', 'Assistant Professor', 'rxiao@mail.med.upenn.edu'"]),
# ("('Sharon', 'Xie')",
#  ["'PhD', 'Associate Professor', 'sxie@mail.med.upenn.edu'"]),
# ("('Dawei', 'Xie')", ["'PhD', 'Assistant Professor', 'dxie@upenn.edu'"]),
# ("('Wei', 'Yang')",
#  ["'PhD', 'Assistant Professor', 'weiyang@mail.med.upenn.edu'"])]
