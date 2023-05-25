# import the dog library from python
from dog import Dog, Treat

# create a dog
my_dog = Dog("Tim")

# create a treat
treat = Treat("Watermelon", 100)

# give your dog some more treats (like a lot they be hungry)
for i in range(0,10):
    my_dog.append(Treat("Kibble", 5))

# index the dog
my_dog.append(treat)
print(my_dog[0])

my_dog.append(Treat("Blueberries", 200))
print(my_dog[1])

# transform the dog into an integer
print(my_dog)
print(str(int(my_dog)))

# make a new dog and check if it's equal!
other_dog = Dog("John")
same_dog = Dog("Tim")
print(other_dog == my_dog)
print(same_dog == my_dog)

# tell it to say grace!
my_dog.say_grace()