n = int(input("Enter the limit - "))

start_val = n*(n+1)/2
for i in range(n,0,-1):
    start_val -= i-1 if i==n else i
    inner = ""
    c = int(start_val)
    for j in range(i):
        inner += str(c)+"\t"
        c += 1
    print(inner)
    