#%%
## This file contails various demos for python 3.9

# here I have imported various modules that we will use thrughout this demo.
import math
import os
import random

#Variables can hold many data types such as strings, numbers, lists, dictionaries, and more!
Sample_Variable = "I am a sample variable"
Sample_number_variable = 10
Sample_List = [1,2,"pie",math.pi]
Sample_dictionary = {"name": "Car", "Color": "blue", "speed": 0}
count = 0

#A variable may also store an expression, esentialy a compund variable that does comonly does something basic.
Sample_expression = "sample" + " expression"

#Conditionals are logic stamtements that compare variables and do something with the result.
if Sample_number_variable == 10:
    print("The sample number variable is 10!")
else:
    print("The sample number variable is not equal to 10!")

#Loops are usefull for repetedly performing an action.
for item in Sample_List:
    print(item)

while count <= 10:
    print(count)
    count += 1

#functions are groupings of code you want to be able to use in many places, like a macro.  
def Do_A_Thing():
    print("I did a thing!")

def Do_Math(number_in):
    return(number_in + 1)

#python is an object oriented programing language, and classes are a perfect example of that
class Car_Data:
    speed = 0
    color = "blue"

    def accelerate(self):
        self.speed += 1
        
    def repaint(self):
        self.color = input("what color should the car be?   ")

#python can be used for many applications past simple calculations and data storage.  Fore example, File manipulaion.

class filewriter:

    def __init__(self):
        self.Working_Folder = os.path.dirname(os.path.realpath(__file__))

    def create_file(self,filename):
        file = open(f"{self.Working_Folder}/{filename}.txt","x")
        file.close()

    def write_to_file(self,filename,text):
        work_file = open(f"{self.Working_Folder}/{filename}.txt","w")
        work_file.write(text)
        work_file.close

    def append_to_file(self,filename,text):
        work_file = open(f"{self.Working_Folder}/{filename}.txt","a")
        work_file.write(text)
        work_file.close


# this is a demo funciton that ties together pieces from accross this program
def Demo_Wrapup():
    fw = filewriter()
    car = Car_Data()
    speeds = [5,25,100]

    speed = random.choice(speeds)

    while car.speed != speed:
        car.accelerate()

    if speed < 25:
        fw.create_file("speeding report")
        fw.write_to_file("speeding report",f"A person in a {car.color} car was driving at {car.speed} Miles an hour. A warning was issued")
    if speed == 25:
        print("no report needed!")   
    if speed > 25:
        fw.create_file("speeding report")
        fw.write_to_file("speeding report",f"A person in a {car.color} car was driving at {car.speed} Miles an hour. they were given a tiket")        

# %%
