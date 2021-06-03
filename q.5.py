#q.5: Write a Python program that takes a text file as input and returns the number ofwords of a given text file.

count = 0;  
   
class wordcount:
    
    def __init__(self,f):
        self.myfile=f
    def wordfile(self):
        count=0
        for i in self.myfile:
            w=i.split(" "+","+"")
            count=count+len(w)
        print("Number of words"+str(count))
        self.myfile.close()   
        

file=open("myfile.txt",'r')
a=wordcount(file)
a.wordfile()