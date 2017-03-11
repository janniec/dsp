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

# writing to csv
df['email'].to_csv('emails.csv', mode = 'w', index = False)

# verify that it wrote right
emails_file = pd.read_csv("emails.csv", header=None)
print emails_file



