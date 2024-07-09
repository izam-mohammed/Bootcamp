from abc import abstractmethod, ABC

class Calculator:
    def __init__(self, id, name): 
        self.id = id 
        self.name = name
        
    @abstractmethod
    def add(self, num1, num2):
        pass
    
    @abstractmethod
    def substract(self, num1, num2):
        pass
    
    @abstractmethod
    def multiply(self, num1, num2):
        pass
    
    @abstractmethod
    def devide(self, num1, num2):
        pass
    
class newCalc(Calculator):
    def add(self, num1, num2):
        return num1+num2
    
    def substract(self, num1, num2):
        return num1-num2
    
    def multiply(self, num1, num2):
        return num1*num2
    
    def devide(self, num1, num2):
        return num1/num2
    
calc = newCalc(1,"hisham")
print(calc.add(5,6))


