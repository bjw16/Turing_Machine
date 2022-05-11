#!/bin/env python3
import sys

#checks arguments
if(len(sys.argv) != 2):
	print('Usage:', sys.argv[1], 'string')
	sys.exit(1)

#input contains the input string
input = [] 
input[:0] = sys.argv[1]

#variable that iterates through the input
readHead = 0

#represents control unit (T/F)
controlUnit1 = None
controlUnit2 = None

#iteration of the loop
timestep = 1

#passed the '#' symbol
passed = False

#variable to determine if input was accepted or rejected
accepted = None

#left
left = False

#last
last = False

#first Scan, checks to see if string is even valid
while(1):
	#prints what step we are on
	print("Read/Write Head: ", readHead)
	print("Loop iteration: ", timestep)
	#increment by 1
	timestep+= 1
	
	#checks if at starting position
	if readHead == 0:
		#checks if '#' at beginning and rejects if string after '#'
		#accepts if only '#'
		if input[readHead] == '#':
			passed = True
			#checks if pointer is out of bounds
			#means string is onl # which is accepted
			if readHead + 1 == len(input):
				#accept
				accepted = True
				break
			#increment if not
			readHead += 1
		#This means that the input is either a 1 or a 0
		#We begin by setting control to either true or false
		#depending on if current input is a 1 or 0
		#and insert a x in its place
		else:
			#adds first variable to control Unit
			if input[readHead] == '1':
				controlUnit1 = True
			else:
				controlUnit1 = False

			#copies string and insert x
			newString = ""
			for i in range(len(input)):
				if i == 0:
					newString += 'x'
				else:
					newString += input[i]
			input = newString

			#checks if next variable is nothing
			if readHead + 1 == len(input):
				#reject because it is out of format
				accepted = False
				break
			else:
				readHead+=1
	#means we are not on first iteration
	else:
		#checks to see if we passed the '#'
		if passed != True:
			#checks to see if current position is '#'
			if input[readHead] == '#':
				passed = True
				#checks to see if there is a string beyon '#'
				if readHead + 1 == len(input):
					#reject because no number after #
					accepted = False
					break
				readHead += 1
			#if not '#', we increment to next spot
			else:
				#checks to see if string ends before '#'
				if readHead + 1 == len(input):
					accepted = False
					break
				else:
					readHead += 1
					continue
		#if past hash, we must now look for the matching control Unit
		else:
			#checks if current spot is a 1 or a 0
			if controlUnit1 == None:
				accepted = False
				break
			elif input[readHead] == '1':
				controlUnit2 = True
			else:
				controlUnit2 = False
			#compares both control Units
			if controlUnit1 == controlUnit2:
				#continue with turing machine

				#adds x into current position
				newString = ""
				for i in range(len(input)):
					if i == readHead:
						newString += 'x'
					else:
						newString += input[i]
				input = newString
				#resets variables
				controlUnit1 = None
				controlUnit2 = None
				break

			else:
				#reject because to controls dont match
				accepted = False
				break

#reduces by 1 and changes directions left
readHead += -1
left = True


#should lead to finding second x
while(accepted == None):
	#prints to show what increment we are on
	print("Read/Write Head: ", readHead)
	print("Loop iteration: ", timestep)
	timestep+= 1
	
	#changes passed to false when passing '#' from the left
	if passed == True and left == True:
		if input[readHead] == '#':
			passed = False
		#continues to go left
		readHead -= 1
		continue

	#continue left until hit a 'x' in the spot before this one
	if passed == False and left == True and input[readHead] != 'x':
		#checks if the input before this was x
		if input[readHead-1] == 'x':
			#changes variable because we are going right
			left = False
		
			#sets control Unit 1
			if input[readHead] == '1':
				controlUnit1 = True
			else:
				controlUnit1 = False
			#copies string with x inserted
			newString = ""
			for increment in range(len(input)):
				if increment == readHead:
					newString += 'x'
				else:
					newString += input[increment]
			input = newString

			#increments head by 1
			readHead += 1
		
			#checks if this is the last control to compare
			if input[readHead] == '#':
				last = True
		#continue left and hopefully next loop we run into a 'x'		
		else:
			#makes sure to stay in bounds
			if readHead - 1 > 0:
				readHead -= 1

	#check if current spot is a '#' after inserting x
	if passed == False and controlUnit1 != None and left == False:
		if input[readHead] == '#':
			passed = True
		
		#increments no matter what
		readHead += 1
		continue

	#checks to see if there is a variable ready to compare with control unit.
	if passed == True and left == False:
		#checks if currently we are at a x, if so, we move on
		if input[readHead] == 'x':
			#checks if we can't compare because string suddenly ends
			if readHead + 1 == len(input):
				#reject because can't go any farther
				accepted = False
				continue
			else:
				readHead += 1
		#Checks if we can compare control Units
		else:
			#compares control units
			if input[readHead] == '1':
				controlUnit2 = True
			else:
			 	controlUnit2 = False
			if controlUnit1 == controlUnit2:
				#send back the other way and reset variables
				left = True
				controlUnit1 = None
				controlUnit2 = None
				
				#inserts x
				newString = ""
				for increment in range(len(input)):
					if increment == readHead:
						newString += 'x'
					else:
						newString += input[increment]
				input = newString
 
				#determines if that was the last compare, if so end
				if last == True:
					accepted = True
					continue
				readHead -= 1
			#rejected
			else:
				accepted = False
	continue




if accepted == True:
	print("ACCEPTED")
elif accepted == False:
	print("REJECTED\n")
