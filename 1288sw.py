test=int(input())

for t in range(test):
    n=int(input())

    array=[]
    ans=[0,1,2,3,4,5,6,7,8,9]
    count=1
    while array!=ans :
        for i in str(n*count):
            if int(i) not in array:
                array.append(int(i))
        array.sort()
        if array==ans:
            break
        count+=1

    print("#{} {}".format(t+1,count*n))