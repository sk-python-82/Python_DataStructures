class Stack():
    def __init__(self):
        self.objects = [] 
#this method will add an item to the end of the stack
    def push(self,i):
        self.objects.append(i) 
#this method will delete an item from the stack by taking the index
    def pop(self,indexx):
        if len(self.objects) == 0:
            print("your stack doesnt have any object,push one in to pop it")
        else:
            return self.objects.pop(indexx)
#this method will print whole objects inside the stack after pushs and pops
    def prrint(self):
                print(self.objects)
#this method searches the stack for the element we want
    def search(self,data2):
         for i in self.objects:
              if i == data2 :
                   print("found object location,object is located at following index:"+str(self.objects.index(i)))  
#this method will tell us if stack is empty or not
    def empty(self):
         if len(self.objects) == 0:
              print("your stack is empty,use push method to add elements to it!") 
         else:
              print("your stack is not empty, your stack is:" + str(self.objects)) 
              
#this method will tell usthe size of the stack
    def size(self):
         print("this is the length of your stack"+str(len(self.objects))) 
#Next method is used to tell us what is the latest added element
    def peek(self):
         counter = -1
         for i in self.objects:
              counter += 1 
         peeek = self.objects[counter]
         print("this is your peek:" +str(peeek))
           
        
                   
s = Stack()
s.push(10)
s.push("sina")
s.push(20)
s.pop(2)
s.prrint()
s.search("sina")
s.size()
s.empty()
s.peek()

    




