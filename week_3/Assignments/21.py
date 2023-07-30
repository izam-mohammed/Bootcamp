class Home:
    def __init__(self):
          pass 
    def room1(self): 
         width=100 
         breadth = 100 
         print('are of room1',width*breadth) 
    def kitchen(self): 
         width = 1222
         breadth = 4888 
         print('are of kitchen',width*breadth) 

class FirstHome(Home):
    def studyroom(self):
        width = 500
        breadth = 600
        print('are of study room',width*breadth)
        
class SecondHome(Home):
    def workarea(self):
        width = 500
        breadth = 600
        print('are of study room',width*breadth)
        
if __name__ == "__main__":
    first = FirstHome()
    first.kitchen()
