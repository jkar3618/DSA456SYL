'''
Name: Taehwa Hong
Student ID: 132546227
'''

def function1(number):
	total = 0   # 1
    			# variable initialization: 1 operation
 
	for i in range(number): # n + 1
					        # 1 operation for calling the range function
					        # the loop runs number times
							
		x = i + 1   # 2n
					# addition (i + 1): 1 operation
					# assignment to x: 1 operation
					# total 2 operations for each iteration
					
		total += x * x  # 3n
					# multiplication (x * x):  1 operation
					# addition (total += x * x): 1 operation
					# assginment to total: 1 operation
					# total 3 operations for each iteration

 
	return total    # 1
			# return: 1 operation

	# 1 + n + 1 + 2n + 3n + 1
	# 6n + 3
	# O(n)
	
def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6  # 6 operations
							# Multiplication operation: 3
							# Addition operation: 2
							# Division operation: 1
							# 3 + 2 + 1
							# 6
							# O(1)

def function3(list):
	n = len(list)
	for i in range(n - 1):  # outer loop: n - 1
		for j in range(n - 1 - i):  # inner loop: n - 1 - i
			if list[j] > list[j+1]: # 1
				tmp = list[j]       # 1
				list[j] = list[j+1] # 1
				list[j + 1] = tmp   # 1
				
# It is nested loop. So, time complexity is O(n²)

def function4(number):
	total = 1   # 1
	for i in range(1, number):  # n - 1
		total *= i + 1  # 1
	return total    # 1
# 1 + (n-1) + 1 + 1
# n + 2
# O(n)



########## Part B #########

def sum_to_goal(numbers, goal):
    seen = set()

    for num in numbers:
        complement = goal - num

        if complement in seen:
            return num * complement
        seen.add(num)

    return 0

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current