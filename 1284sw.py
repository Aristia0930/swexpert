test=int(input())

for t in range(test):
    p,q,r,s,w=map(int,input().split())
    wa=p*w

    wb=0
    if w<=r:
        wb=q
    else:
        wb=(w-r)*s+q
    print("#{} {}".format(t+1,min(wa,wb)))
