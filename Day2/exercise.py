#Work with some data types in python
two_digit_number = input("Type a two digit number: ")

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

answer = first_num + second_num

print(str(first_num) + " + " + str(second_num) + " is equal to " + str(answer))

#Division makes the data type a float
num = 6/3
print(num)

#Python follows PEMDAS rule here is an example.
print(3 *( 3 + 3) / 3 - 3**3)