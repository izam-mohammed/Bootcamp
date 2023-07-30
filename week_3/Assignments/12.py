limit = int(input("Enter the limit of array - "))
print("Enter the elements in array 1 - ")
array1 = list()
for i in range(limit):
    innerarr= list()
    for j in range(limit):
        innerarr.append(int(input()))
    array1.append(innerarr)
    
print("Enter the elements in array 2 - ")
array2 = list()
for i in range(limit):
    innerarr= list()
    for j in range(limit):
        innerarr.append(int(input()))
    array2.append(innerarr)
    
print("Sum of 2 array is - ")
for i in range(limit):
    innerarr = ""
    for j in range(limit):
        innerarr+= str(array1[i][j]+array2[i][j])+"\t"
    print(innerarr)