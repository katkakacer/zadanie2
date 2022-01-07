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

def mysimplify(f):
    if type(f)==float or type(f)==int:
        return myevald(f,{})

    if type(f)==str:
        return f

    if type(f)==list:
        

        if f[0]=='+':
            x1=mysimplify(f[1])
            x2=mysimplify(f[2])

            if x1==0:
                return x2
            elif x2==0:
                return x1
            else:
                return ["+",x1,x2]

        if f[0]=="*":
            x1=mysimplify(f[1])
            x2=mysimplify(f[2])

            if x1==1:
                return x2
            elif x2==1:
                return x1
            elif x1==0 or x2==0:
                return 0
            else:
                return ["*",x1,x2]

        if f[0]=='/':
            x1=mysimplify(f[1])
            x2=mysimplify(f[2])

            if x2==1:
                return mysimplify(f[1])
            else:
                return ["/",x1,x2]

        if f[0]=='-':
            return ['-',mysimplify(f[1]),mysimplify(f[2])]


if __name__=="__main__":
    print(mysimplify(['+','x',1]))