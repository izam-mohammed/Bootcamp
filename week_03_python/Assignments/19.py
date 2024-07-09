def getArray(arr, limit):
    print("Enter the array elements - ")
    for i in range(limit):
        inner = list()
        for j in range(limit):
            inner.append(int(input()))
        arr.append(inner)
        
def display(arr, limit):
    inner = ""
    for i in range(limit):
        inner = ""
        for j in range(limit):
           inner+=str(arr[i][j])+"\t"
        print(inner)

if __name__ == "__main__":
    limit = int(input("Enter the limit - "))
    arr = list()
    getArray(arr, limit)
    display(arr, limit)