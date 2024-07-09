limit = int(input("Enter the size of the array - "))
print("Enter the elements in that array - ")
arr = []
for i in range(limit):
    arr.append(int(input()))
    
#sorting
for i in range(limit):
    for j in range(0,i+1):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            
print(f"sorted array - {arr}")