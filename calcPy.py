#!urs/bin/python3
import os
import time
import numpy as np

def print_number_options():
	print("\x1b[1;33m"+"Which operation do you wanna do?")
	print("""Please select the number of the operation."""+"\033[;36m"+"""
        \n  1. Add
        \n  2. Sub
        \n  3. Mult
		\n  4. Square
        \n  5. Cube
		\n	Option: """, end='')

def print_options():
	print("\x1b[1;33m"+"Which operation do you wanna do?")
	print("""Please select the number of the operation."""+"\033[;36m"+"""
        \n  1. Mult
		\n  2. Square
        \n  3. Cube
		\n	Option: """, end='')

#--------------------------- Number type ------------------------------#

def number():
	print_number_options()
	number_operation = {
		'1' : number_add,
		'2' : number_sub,
		'3' : number_mul,
		'4' : number_square,
		'5' : number_cube
	}
	operation = input()
	clear()
	number_operation[operation]()

def number_add():
	print("\x1b[1;33m"+"Please enter two numbers: \n" +"\033[;36m"+ "Operator 1: ", end='')
	a = input()
	print("Operator 2: ",end='')
	b = input()
	print("\033[4;35m"+"Result: %s + %s = %s" %(a, b, str(int(a) + int(b))))
	time.sleep(5)
	clear()

def number_sub():
	print("\x1b[1;33m"+"Please enter two numbers: \n"+"\033[;36m"+"Operator 1: ", end='')
	a = input()
	print("Operator 2: ",end='')
	b = input()
	print("\033[4;35m"+"Result: %s - %s = %s" %(a, b, str(int(a) - int(b))))
	time.sleep(5)
	clear()

def number_mul():
	print("\x1b[1;33m"+"Please enter two numbers: \n"+"\033[;36m"+"Operator 1: ", end='')
	a = input()
	print("Operator 2: ",end='')
	b = input()
	print("\033[4;35m"+"Result: %s * %s = %s" %(a, b, str(int(a) * int(b))))
	time.sleep(5)
	clear()

def number_square():
	print("\033[;36m"+"Please enter a base: ", end='')
	base = input()
	print("\033[4;35m"+"Result: %s ^ 2 = %s" %(base, str(int(base) ** 2)))
	time.sleep(5)
	clear()

def number_cube():
	print("\033[;36m"+"Please enter a base: ", end='')
	base = input()
	print("\033[4;35m"+"Result: %s ^ 3 = %s" %(base, str(int(base) ** 3)))
	time.sleep(5)
	clear()

#--------------------------------- List type -----------------------------------#

def lista():
	print_options()
	list_operation = {'1' : list_mul, '2' : list_square, '3' : list_cube}
	operation = input()
	clear()
	list_operation[operation]()

def list_mul():
	print("\033[;36m"+"Please enter the length of the list: ", end='')
	lenght = input()
	lis = []
	print("Please enter the values of the list.")
	for i in range(int(lenght)):
		lis.append(input())
	print(lis)
	print("Enter the number to mult: ", end='')
	a = input()
	for i in range(len(lis)):
		lis[i] = int(lis[i]) * int(a)
	print("\033[4;35m"+"The result is: ", end='')
	print(lis)
	time.sleep(5)
	clear()

def list_square():
	print("\033[;36m"+"Please enter the length of the list: ", end='')
	lenght = input()
	lis = []
	print("Please enter the values of the list.")
	for i in range(int(lenght)):
		lis.append(input())
	print(lis)
	for i in range(len(lis)):
		lis[i] = int(lis[i]) ** 2
	print("\033[4;35m"+"The result is: ", end='')
	print(lis)
	time.sleep(7)
	clear()

def list_cube():
	print("\033[;36m"+"Please enter the length of the list: ", end='')
	lenght = input()
	lis = []
	print("Please enter the values of the list.")
	for i in range(int(lenght)):
		lis.append(input())
	print(lis)
	for i in range(len(lis)):
		lis[i] = int(lis[i]) ** 3
	print("\033[4;35m"+"The result is: ", end='')
	print(lis)
	time.sleep(7)
	clear()

#---------------------------------------- Array type ------------------------------------#

def array():
	print_options()
	array_operation = {
		'1' : array_mul,
		'2' : array_square,
		'3' : array_cube
	}
	operation = input()
	clear()
	array_operation[operation]()

def array_mul():
	print("\x1b[1;33m"+"Please enter the order of the array with two integers\nlike this (first integer(rows) X second integer(cols)): ")
	print("\033[;36m"+"Fisrt integer: ", end='')
	m = input()
	print("Second integer: ", end='')
	n = input()
	print("Enter the values of the array by its index:")
	arr = []
	for i in range(int(m)):
		arr.append([])
		for j in range(int(n)):
			print("[%d][%d]: " %(i,j), end='')
			arr[i].append(int(input()))
	arr = np.array(arr)
	print()
	print(arr)
	print("\nEnter the number you will multiply by the array: ", end='')
	a = input()
	print("\033[4;35m"+"The reult is: ")
	print(arr * int(a))
	time.sleep(8)
	clear()

def array_square():
	print("\x1b[1;33m"+"Please enter the order of the array with two integers\nlike this (first integer(rows) X second integer(cols)): ")
	print("\033[;36m"+"Fisrt integer: ", end='')
	m = input()
	print("Second integer: ", end='')
	n = input()
	print("Enter the values of the array by its index:")
	arr = []
	for i in range(int(m)):
		arr.append([])
		for j in range(int(n)):
			print("[%d][%d]: " %(i,j), end='')
			arr[i].append(int(input()))
	arr = np.array(arr)
	print()
	print(arr)
	print("\033[4;35m"+"\nThe result is:\n")
	print(arr ** 2)
	time.sleep(8)
	clear()

def array_cube():
	print("\x1b[1;33m"+"Please enter the order of the array with two integers\nlike this (first integer(rows) X second integer(cols)): ")
	print("\033[;36m"+"Fisrt integer: ", end='')
	m = input()
	print("Second integer: ", end='')
	n = input()
	print("Enter the values of the array by its index:")
	arr = []
	for i in range(int(m)):
		arr.append([])
		for j in range(int(n)):
			print("[%d][%d]: " %(i,j), end='')
			arr[i].append(int(input()))
	arr = np.array(arr)
	print()
	print(arr)
	print("\033[4;35m"+"\nThe result is:\n")
	print(arr ** 3)
	time.sleep(8)
	clear()

def clear():
	"""
	This method clean the console output.
	"""
	if os.name == "posix":
		os.system ("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system ("cls")

operation_options = {
	'1' : number,
	'2' : lista,
	'3' : array
}

while True:
	print("\x1b[1;33m"+"Which data type do you want to operate?")
	print("""Please select the number of the data type:"""+"\033[;36m"+"""
		\n  1. Number
		\n  2. List
        \n  3. Array
        \n  0. Exit
		\n	Option: """, end='')

	operation = input()
	if operation == '0':
		break

	clear()
	operation_options[operation]()

clear()
print("Calc off")