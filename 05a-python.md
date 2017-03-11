# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that both are sequences of elements. They differ in that lists are modifiable but tuples, once entered, are not.  
Only tuples can work as keys in a dictionary because only immutable elements should be used as dictionary keys. Dictionaries map keys to values. Programs using dictionaries build on the reliability of calling keys and expecting specific values. The mutability of keys, as in a list, could cause the values to also change, which would lead to unexepcted behaviors in the programs.  


---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that both are collections of elements. They differ in that the elements within a set must be unique from each other and are unordered.  
List = [‘aye’, ‘bee’, ‘sea’, ‘dee’, ‘ee’, ‘eff’, ‘gee’]  
Set  = set([‘eche’, ‘eye’, ‘jay’, ‘kaye’, ‘elle’, ‘em’])  
We can find an element within in a list by indices because lists can be sorted and have positions. However, because a set does not record positions or orders of insertion, an element within sets are found through operations such as ‘intersection’, ‘union’, ‘difference’, and ‘symmetric’.  

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> ‘lambda’ is a single expression function. It is used for nesting small functions within other functions.  For example, 
mult3 = filter(lambda x:  x % 3 == 0, range(1, 10))  
will give you [3, 6, 9]. Another example,  
print sorted(['Upper', 'case', 'usually', 'sorts', 'first'])  
will return ['Upper', 'case', 'first', 'sorts', 'usually']. To sort regardless of upper or lower cases, use  
print sorted(['Upper', 'case', 'usually', 'sorts', 'first'], key=lambda word: word.lower())  
which will give you ['case', 'first', 'sorts', 'Upper', 'usually'].  

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are applications that create new lists where each element is the result of operations. For example,  
list_comp = []  
for x in range(10):  
    list_comp.append(x * 2)  
print list_comp  
  
>> Filter will apply a function to a sequence, returning True or False for each element, and ultimately return a list of only members of the sequence for which the function returned True.  For example,  
filter_comp = filter(lambda x: x % 2 == 0, range(20))  
print filter_comp  
  
>> Map will apply a supplied function to each element of the sequence and return a list of results for each element. For example,  
map_comp = map(lambda x: x * 2, range(10))  
print map_comp  
  
>> More examples, a set comprehension and a dictionary comprehension  
set_comp = set(n * 2 for n in range(10))  
print set_comp  
dict_comp = {x:  x * 2 for x in range(10)}  
print dict_comp 

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> from datetime import datetime  
date_start = datetime.strptime('01-02-2013', "%m-%d-%Y")  
date_stop = datetime.strptime('07-28-2015', "%m-%d-%Y")  
print abs((date_stop - date_start).days)  

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> from datetime import datetime  
date_start = datetime.strptime('12312013', "%m%d%Y")  
date_stop = datetime.strptime('05282015', "%m%d%Y")  
print abs((date_stop - date_start).days) 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> from datetime import datetime  
date_start = datetime.strptime('15-Jan-1994', "%d-%b-%Y")  
date_stop = datetime.strptime('14-Jul-2015', "%d-%b-%Y")  
print abs((date_stop - date_start).days)  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





