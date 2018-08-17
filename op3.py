#!/usr/bin/python2

import  webbrowser 

print  "opening  default web browser "
webbrowser.open_new_tab('https://www.google.com')

print  "plz wait returing to main file "
time.sleep(2)
execfile('/tmp/a.py')

