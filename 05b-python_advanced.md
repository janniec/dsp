# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> import pandas as pd  
import numpy as np  
from pprint import pprint  
import csv    
import ast  
  
>> url = "https://raw.githubusercontent.com/thisismetis/dsp/master/python/faculty.csv"  
df = pd.read_csv(url)  
    
>> df.info()   
df = df.rename(columns={' degree': 'degree'})  
df = df.rename(columns={' title': 'title'})  
df = df.rename(columns={' email': 'email'})  
df.info()  
  
>> df['degree'].unique()  
df['degree'] = df['degree'].str.replace('.', '') # remove the periods  
df['degree'] = df['degree'].map(lambda x: x.strip())  
   
>> deg_copy = df.copy()  
dum_degree = pd.concat([deg_copy, df['degree'].str.get_dummies(sep=' ')], axis=1)  
    
>> dum_degree.ix[:, 4:].sum()  
  
>> ANSWER:   
 0        1  
 BSEd     1  
 JD       1  
 MA       1  
 MD       1  
 MPH      2  
 MS       2  
 PhD     31  
 ScD      6  
 dtype: int64 


#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> df['title'].unique()  
    
>> df['title'] = df['title'].str.replace(' is ', ' of ') # correct the title  
df['title'] = df['title'].str.replace(' of Biostatistics', '')  
   
>> tit_copy = df.copy()  
tit_dum = pd.get_dummies(df.title)  
dum_title = pd.concat([tit_copy, tit_dum], axis=1)  
  
>> dum_title.ix[:, 4:].sum()    
  
>> ANSWER:   
 Assistant Professor    12  
 Associate Professor    12  
 Professor              13  
 dtype: int64  



#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> print df['email'].tolist()  
  
>> ANSWER:  
 ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu',   
 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu',   
 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu',   
 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu',   
 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu',   
 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu',   
 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu',   
 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu',   
 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu',   
 'weiyang@mail.med.upenn.edu']  


#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> domain = df['email'].map(lambda x: x.split('@')[1])    
domain.unique()  
domain.nunique()  

>> ANSWER: 4  

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> df['last_name'] = df.name.str.split('\s+').str[-1]  
   
>> dte_df = df[['degree', 'title', 'email']].copy()  
dte_df.update("'" + df[['degree', 'title', 'email']] + "'") # within quotes  
dte_df['dte'] = dte_df.apply(lambda row: ', '.join(map(str, row)), axis=1)  
    
>> facu_df = pd.concat([df['last_name'], dte_df['dte']], axis=1)  
facu_df.update("[" + facu_df['dte'].astype(object) + "]")  
  
>> faculty_dict = dict(facu_df.groupby('last_name')['dte'].apply(list))  
  
>> faculty3pairs = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}  
faculty3pairs  
  
>> ANSWER:  
 {'Bilker': ["['PhD', 'Professor', 'warren@upenn.edu']"],  
 'Feng': ["['PhD', 'Assistant Professor', 'ruifeng@upenn.edu']"],  
 'Putt': ["['PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu']"]}  

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> fl_df = df[['first_name', 'last_name']].copy()  
fl_df.update("'" + fl_df[['first_name', 'last_name']] + "'")  
fl_df['first_last'] = fl_df.apply(lambda row: ', '.join(map(str, row)), axis=1)  
  
>> prof_df = pd.concat([fl_df['first_last'], dte_df['dte']], axis=1)  
prof_df.update("(" + prof_df['first_last'].astype(str) + ")")  
   
>> professor_dict = prof_df.set_index('first_last').T.to_dict('list')  
professor_dict    
    
>> professor3pairs = {k: professor_dict[k] for k in sorted(professor_dict.keys())[:3]}  
professor3pairs  
  
>> ANSWER:  
 {"('A.', 'Localio')": ["'JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu'"],  
 "('Alisa', 'Stephens')": ["'PhD', 'Assistant Professor', 'alisaste@mail.med.upenn.edu'"],  
 "('Andrea', 'Troxel')": ["'ScD', 'Professor', 'atroxel@mail.med.upenn.edu'"]}  

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> pprint(sorted(professor_dict.items(),  
              key=lambda x: str(x[0].split(" ")[1])))  

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

