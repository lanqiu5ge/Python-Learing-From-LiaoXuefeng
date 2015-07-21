#usr/bin/env python
#-*- coding:utf-8 -*-
def hanoi(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    hanoi(n-1, a, c, b)
    print('move', a, '-->', c)
    hanoi(n-1, b, a, c)
hanoi(4, 'A', 'B', 'C')
