# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

from datetime import datetime
date_start = datetime.strptime('01-02-2013', "%m-%d-%Y")
date_stop = datetime.strptime('07-28-2015', "%m-%d-%Y")
print abs((date_stop - date_start).days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime
date_start = datetime.strptime('12312013', "%m%d%Y")
date_stop = datetime.strptime('05282015', "%m%d%Y")
print abs((date_stop - date_start).days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from datetime import datetime
date_start = datetime.strptime('15-Jan-1994', "%d-%b-%Y")
date_stop = datetime.strptime('14-Jul-2015', "%d-%b-%Y")
print abs((date_stop - date_start).days)
