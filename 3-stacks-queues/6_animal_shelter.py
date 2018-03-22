# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based
# on arrival time) of all animals at the shelter, or they can select whether
# they would prefer a dog or a cat (and will receive the oldest animal of that
# type). They cannot select which specific animal they would like. Create the data 
# structures to maintain this system and implement operations such as enqueue,
# dequeueAny, dequeueDog, and dequeueCat. You may use the bult-in LinkedList
# data strucuture.

from linked_list import LinkedList

class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type
    
    def __eq__(self, other):
        return self.animal_type == other.animal_type
    
    def __str__(self):
        return str(self.animal_type)

class Shelter:
    def __init__(self):
        self.animals = LinkedList()

    def enqueue(self, animal):
        self.animals.insert(animal)
    
    def dequeue_any(self):
        return self.animals.popright()
    
    def dequeue_dog(self):
        dog = Animal("dog")
        dog_node = self.animals.search_right(dog)
        if dog_node:
            self.animals.delete_right(dog, dog_node)
        return dog_node.item
    
    def dequeue_cat(self):
        cat = Animal("cat")
        cat_node = self.animals.search_right(cat)
        if cat_node:
            self.animals.delete_right(cat, cat_node)
        return cat_node.item
    
    def __str__(self):
        return str(self.animals)

if __name__ == '__main__':
    x = Shelter()
    x.enqueue(Animal("cat"))
    x.enqueue(Animal("dog"))
    print(x)
    print(x.dequeue_any())
    print(x)
    x.enqueue(Animal("cat"))
    x.enqueue(Animal("cat"))
    x.enqueue(Animal("cat"))
    print(x)
    print(x.dequeue_cat())
    print(x)
    print(x.dequeue_dog())
    print(x)
    print(x.dequeue_any())
    print(x)