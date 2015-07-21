#usr/bin/env python
#-*-coding:utf-8-*-

def hello (greeting, *args):
    if(len(args)==0):
        print '%s' % greeting
    else:
        print '%s, %s' % (greeting, ', '.join(args))

hello('Hi')
hello('Hi', 'Lisa')


