#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class pet:
    animal = ""
    breed = ""
    name = ""
    owner = ""
    birth = ""

    def __init__(self):
        self.animal = input("What kind: ")
        self.breed = input("Breed type: ")
        self.name = input("Name: ")
        self.owner = input("Owner's name: ")
        self.birth = input("Birthdate: ")

    def display(self):
        print("Name: " + self.name)
        print("Type: " + self.animal)
        print("Breed: " + self.breed)
        print("Owner: " + self.owner)
        print("Bday: " + self.birth)

def main():

    animals=[]
    num = 0

    while True:

        print("OPTIONS: ")
        print("1: Enter a new pet")
        print('2: Retrieve a pet')
        print('3: Exit')
        num=int(input())

        if num == 1:
            animals.append(animal())

        if num == 2:
            ind=input('Name: ')
            length=len(animals)
            for x in range(0,length):
                name=animals[x].name
                if name==ind:
                    animals[x].display()
                
        if num == 3:
            print('Closing Program')
            break