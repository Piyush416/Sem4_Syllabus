# maximum of three

def max_three(a):
    arr_size = len(a)
    first = second = third = -23423423
    for i in range(0,arr_size):
        if a[i]>first:
            third = second
            second = first
            first = a[i]
        elif (a[i]>second and a[i]!=first):
            third = second
            second = a[i]
        elif (a[i]>third and a[i]!=first and a[i]!=first):
            third = a[i]

    print("Three Greatest Number is:",third,second,first)

a = [12,12,13,1,10,34,34,34,1]
max_three(a)

