#!/usr/bin/env python3

def myevald(x,d):

    if type(x)==int or type(x)==float:
        return x

    if type(x)==str:
        return d[x]

    if type(x)==list:

        for var in x:
            if type(var)==list:
                var=myevald(var,d)

        if x[0]=='+':
            return myevald(x[1],d)+myevald(x[2],d)
        elif x[0]=='-':
            return myevald(x[1],d)-myevald(x[2],d)
        elif x[0]=='*':
            return myevald(x[1],d)*myevald(x[2],d)
        elif x[0]=='/':
            return myevald(x[1],d)/myevald(x[2],d)