test=int(input())

for t in range(test):
    n=int(input())
    now_speed=0
    ans=0
    for i in range(n):
        array=list(map(int,input().split()))
        if array[0]==0:
            ans+=now_speed
        if array[0]==1:
            now_speed+=array[1]
            ans+=now_speed
        if array[0]==2:
            now_speed-=array[1]
            if now_speed<0:
                now_speed=0
            ans+=now_speed
    print("#{} {}".format(t+1,ans))
