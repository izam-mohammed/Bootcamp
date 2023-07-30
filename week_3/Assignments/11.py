word = input("Enter a word : ")

flag = 0
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        flag=1
        break

if flag:
    print("It's not a palindrome")
else:
    print("It's a palindrome")
    