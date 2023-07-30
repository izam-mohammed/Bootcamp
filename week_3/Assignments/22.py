class Acc:
    def __init__(self, name, num):
        self.__name = name 
        self.__accNo = num
        
    @property
    def name(self):
        return self.__name
    
    @property
    def acc_no(self):
        return self.__accNo
    
    @name.setter
    def name(self, val):
        self.__name = val
    
    @acc_no.setter
    def acc_no(self, val):
        self.__accNo = val
        
if __name__ == "__main__":
    user1 = Acc("hisham",123)
    print(f"name - {user1.name}")
    user1.acc_no = 965
    print(f"acc no - {user1.acc_no}")