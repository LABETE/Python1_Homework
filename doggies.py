#!/usr/local/bin/python3
"""Program for save Dog name and breed"""

dogs_lst = []

class Dog:
   
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
if __name__ == "__main__":
    while True: 
        name_inp = input("Enter the name of a dog(Press enter key for finish the program): ")
        if not name_inp:
            break
        breed_inp = input("Enter the breed of the dog: ")
        dogs_data = Dog(name_inp,breed_inp)
        dogs_lst.append(dogs_data)
        dog_num = 0
        for i in dogs_lst:
            print("{0}. {1}:{2}".format(dog_num,i.name,i.breed))
            dog_num += 1
        
        
        