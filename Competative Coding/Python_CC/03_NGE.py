# NEXT GREATER ELMENT
a = [30,40,20,10,5,3,50,45]
print("Given array: ",a)
a.sort()
i = 0
while i <len(a)-1:
  if a[i]<a[i+1]:
    print(a[i],"-->",a[i+1])
  i+=1
print(a[i],"-->","None")
    