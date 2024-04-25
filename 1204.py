t=int(input())
for i in range(t):
    k=int(input())
    array=list(map(int,input().split()))
    max_num=-1
    max_count=0
    for j in array:
        a=array.count(j)
        if a>max_count:
            max_count=a
            max_num=j
        elif a==max_count:
            max_num=max(max_num,j)
    print("#{} {}".format(i+1,max_num))