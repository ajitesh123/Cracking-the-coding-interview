#An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. 
#People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
#They cannot select which specific animal they would like. 
#Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.

from collections import deque


class Animal():
    order=1

    def __init__(self):
        self.dog=deque([])
        self.cat=deque([])


    def push(self, item, type):
        if type==1:
            self.id=Animal.order
            self.dog.append((item, self.id))
            Animal.order+=1

        else:
            self.id=Animal.order
            self.cat.append((item, self.id))
            Animal.order+=1
            
    def dequeAny(self):
        if len(self.dog)==0 and len(self.cat)==0:
            return("No Animal")

        elif len(self.dog)==0:
            return(self.cat.popleft())

        elif len(self.cat)==0:
            return(self.dog.popleft())

        elif self.cat[0][1]<self.dog[0][1]:
            return(self.cat.popleft())
        else:
            return(self.dog.popleft())


def main():
    sample=Animal()
    sample.push("lab", 1)
    sample.push("lnb", 1)
    sample.push("lab", 2)
    sample.push("lnb", 2)

    print(sample.dog)
    print(sample.cat)
    print("------------------------Deque Testing ---------------------")
    print(sample.dequeAny())
    print(sample.dequeAny())
    print(sample.dequeAny())
    print(sample.dequeAny())
    print(sample.dequeAny())


if __name__ == '__main__':
    main()

