class math:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        return self.num1+self.num2
    def substraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2
    
if __name__ == "__main__":
    num1 = int(input("Enter 2 numbers - "))
    num2 = int(input())
    result = int(input("What operation do you want \n1 - addition \n2 - substraction\n3 - multiplication\n4 - division\n"))
    
    maths = math(num1,num2)
    if result==1:
        print(f"\nThe result is {maths.addition()}")
    elif result==2:
        print(f"\nThe result is {maths.substraction()}")
    elif result==3:
        print(f"\nThe result is {maths.multiplication()}")
    elif result==4:
        print(f"\nThe result is {maths.division()}")
    else:
        print("\nYou are a fool")