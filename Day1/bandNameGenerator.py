#Create a greeting for the project
name = input('What is your name? \n')
print("Hello " + name)

#Ask the user for the name of the city you grew up in
city = input('What city did you grow up in?\n')

#Ask the user for the name of a pet.
pet = input("List a pet's name here: \n")

#Combined the name of the city and the name of the pet.
band = name + ', \n    your recommended band name is: \n' + city + ' ' + pet
print (band)
#Make sure the cursor shows on a new line.