def added(*args):
    sum=0
    for i in args:
        sum += i
    return sum

print(f"sum of 1,2,3 = {added(1,2,3)}")
print(f"sum of 8,20,2 = {added(8,20,2)}")
print(f"sum of 12.5,3.147,98.1 = {added(12.5, 3.147, 98.1)}")
print(f"sum of 1.1,2.2,5.5 = {added(1.1, 2.2, 5.5)}")
