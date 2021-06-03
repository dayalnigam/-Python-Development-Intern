#4: Write a Python program to sort a list of dictionaries using Lambda.Original list of dictionaries :
'''[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]'''

d=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

class dictsort:
    def __init__(self, dict,name):
        self.dict = dict
        self.name = name
    def sortfunc(self):
        try:
            return print(sorted(self.dict,key=lambda i:i[self.name]))
        except KeyError:
            return print('check the iteration name')
        except TypeError:
            return print('you have entered int which is not iterable')
        

d1=dictsort(d,'color')
d1.sortfunc()




    
        
