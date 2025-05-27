# iterators and generators both are used for better performance and memory managment,
# they doesn't load all the data at one,
# rather than just the one record at time which saves memory

# iterator

class Myclass:
    
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if(self.a < 20):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    

obj = Myclass()
myiter = iter(obj)
# print(myiter)

# generator

def sq():
    n = 1
    while n <= 10: 
        sq = n*n
        yield sq
        n += 1


tensq = sq()

print(tensq.__next__())
print(tensq.__next__())
print(tensq.__next__())

for sq in tensq :  #for is iterator it bydefault create iterator and call them
    print(sq)


