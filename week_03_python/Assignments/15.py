def get_arr(arr, limit):
    print("Enter the values in the array - ")
    for i in range(limit):
        arr.append(int(input()))
        
def display_arr(arr, limit):
    print("Array - ")
    display = ""
    for i in range(limit):
        display += str(arr[i])+"\t"
    print(display)
    
if __name__ == "__main__":
    arr = list()
    limit = int(input("Enter the limit - "))
    get_arr(arr, limit)
    display_arr(arr, limit)