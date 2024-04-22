def nm(a,m,date,array):
    if a==m:
        return print(*date)
    else:
        for i in range(len(array)):
            if array[i] not in date:
                date.append(array[i])
                nm(a+1,m,date)
                date.pop()



n,m=map(int,input().split())

array=list(map(int,input().split()))

array.sort()



nm(0,m,[],array)
