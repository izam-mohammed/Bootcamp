limit = int(input("Enter the size of Array 1 - "))
arr1 = list()
print("Enter the value - ")
for i in range(limit):
    arr1.append(int(input()))

arr2 = arr1.copy()
#adding 100 and 101 to arr2
arr2 += [100,101]

print(f"Array1 = {arr1}")
print(f"Array2 = {arr2}")