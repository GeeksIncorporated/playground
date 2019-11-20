def sdacha(x):
    a=int(x/10)             # 10
    b=int((x-10*a)/5)       # 5
    c=int((x-10*a-5*b)/2)   # 2
    d=(x-10*a-5*b-2*c)      # 1
    print (a, b, c, d)
