def arr(list):
    list2=[]
    b=1
    for i in list:
        while i/10 != 0:
            a=i%10
            b=b*a
            i=i//10
        list2.append(b)
        b=1
    return list2

array=[66,28,19,25,27]
result=arr(array)
for i in result:
    print(i,end=' ')