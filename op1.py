#!/usr/bin/python2

import time

t_out=time.ctime()

#  spliting on behalf of space 
t=t_out.split()
# only picking time  

print  "current time is  :  ",t[3]
print  "current date is  "+t[2]+" "+t[1]+" "+t[-1]

print  "plz wait returing to main file "
time.sleep(2)
execfile('/tmp/a.py')

