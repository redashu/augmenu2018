#!/usr/bin/env python2
import time

options='''
Press  1  to  current time and date : 
Press  2  to  check  RAM and CPU status : 
Press  3  open default web browser  : 
Press  4 open web cam  : 
Press  5 reboot your system  : 
Press  6 search on google  : 
Press  7  scan all currently connect mac address  : 
Press  8  search on google and list top 5 urls  : 
Press  9  logout current system   : 
'''
print  options 
choice=raw_input()

if  int(choice) ==   1 : 
	execfile('/tmp/op1.py')

if  int(choice) ==   3 : 
	execfile('/tmp/op3.py')
else :
	print  "value out of range "







