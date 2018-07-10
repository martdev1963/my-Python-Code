# Program Architecture
# Mac and Linux: /etc/hosts
# Windows: c:\windows\Systems32\drivers\etc

# for windows machines...
#hosts_path="c:\windows\Systems32\drivers\etc\hosts"
#hosts_path=r"c:\windows\Systems32\drivers\etc\hosts"   #... using the r flag to tell python you are passing a real string not a /w special char...
# or use this alternate solution:
#hosts_path="c:\\windows\\Systems32\\drivers\\etc\\hosts" #  using two back slashes...
# for mac and linux machines...
import time
from datetime import datetime as dt # using the namespace dt for a more concise reference name in the code...
hosts_paths = "/etc/hosts"
# redirects to hosts machine...
redirect="127.0.0.1"
# websites to block during specific times of the day...
website_list=["www.facebook.com","facebook.com", "www.twitter.com", "twitter.com"]

# datetime.datetime(2018, 7, 10, 15, 59, 21, 697959) date, hour, minutes, seconds, micro seconds...
# can break script with ctrl c for mac...
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): # checking for working hours...8am to 16:00(4:00pm)

        print("Working Hours... ")
    else:
        print("Fun Hours... ")
    time.sleep(5)
    print("Five seconds have past... " + str(dt.now().second)) # <----TypeError: must be str, not int due to passing dt.now().second)
    # fixed it with str(dt.now().second))...converted int to string with str()...

"""
    File "app3-website-blocker.py", line 28, in <module>
    print("Five seconds have past... " + dt.now().second)
TypeError: must be str, not int
"""


"""------------------------PYTHON SHELL OUTPUT-----------------------------"""

""" python interactive shell
OUTPUT:
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2018, 7, 10, 15, 59, 21, 697959)
>>>
>>> dt.now() < (2016,5,5,8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'datetime.datetime' and 'tuple'
>>>
"""


"""
OUTPUT:
>>> dt.now() < dt(2016,5,5,8)
False
>>>
"""

"""
OUTPUT:
>>> dt.now().year
2018
>>> type(dt.now().year)
<class 'int'>
>>>
"""

"""
OUTPUT:
Five seconds have past... 50
Fun Hours...
Five seconds have past... 55
Fun Hours...
Five seconds have past... 0
Fun Hours...
Five seconds have past... 5
Fun Hours...
Five seconds have past... 10
Fun Hours...
^CTraceback (most recent call last):
  File "app3-website-blocker.py", line 27, in <module>
    time.sleep(5)
KeyboardInterrupt  <-----typed ctrl c...same for Windows...
Martins-iMac:mapping martinbatista$
"""
