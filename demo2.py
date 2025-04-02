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

array=[]
number=int(input("Enter size of array: "))
for  i in range(0,number):
    num = int(input("Enter element: "))
    array.append(num)

# print(arr(array))
   
    

result=arr(array)
for i in result:
        print(abs(i) ,  end="    ")
