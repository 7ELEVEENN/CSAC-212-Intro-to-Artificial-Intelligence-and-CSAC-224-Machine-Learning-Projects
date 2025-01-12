# Delos Santos, Venn P.  // BSCS 2-A
# Problem Set 1.2
# Program that asks for input 3 times using loop then prints the saved inputs

#define class 'Person' with values 'name' and 'birthdate'
class Person:
  def __init__(self, name, birthdate):
    self.name = name
    self.birthdate = birthdate

#list
persons=[]

#for loop
for i in range(3):
  name = input("Enter your Name: ")
  birthdate= input("Enter your birthdate: ")
  print ("\n")
  persons.append(Person(name,birthdate))

#print saved inputs
for person in persons:
    print( person.name, 'was born on' , person.birthdate )