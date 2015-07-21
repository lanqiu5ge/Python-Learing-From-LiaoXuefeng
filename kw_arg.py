#usr/bin/env python
#-*-coding:utf-8-*-

def print_scores(**kw):
    print ('    name socre')
    print ('---------------')
    for name, score in kw.items():
        print ('%10s %d' % (name, score))
    print

print_scores(Adma=99, Lisa=88, Bart=87)

data = {
        'Adam' : 99,
        'Bob' : 100,
        'TOm' : 89
        }
print_scores(**data)
