# Reflection for Lab 3

## Part A: Analysis

### function 1:


```python
def function1(value, number):
	if (number == 0):
		return 1	# 1
	elif (number == 1):
		return value	# 1
	else:
		return value * function1(value, number-1)	# 1 + n -1

# T(n) = 1 + n - 1
# O(n)
```

### function 2:


```python

def recursive_function2(mystring,a, b):
	if(a >= b ):	# 1
		return True	
	else:
		if(mystring[a] != mystring[b]):	# 1
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)	# T(n-2)
# T(n) = 1 + T(n - 2)
# O(n/2)
# O(n)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)
# O(n)
```

### function 3 (optional):


```python
def function3(value, number):
	if (number == 0):	# 1
		return 1
	elif (number == 1):	# 1
		return value
	else:
		half = number // 2	# 1
		result = function3(value, half)	# T(n/2)
		if (number % 2 == 0):	# 1
			return result * result # 1
		else:
			return value * result * result	# 2

# T(n) = T(n/2) + 1
# O(log n)

```

## Part C Reflection

1. Describe how to approach writing recursive functions; what steps do you take?
- When creating a recursive function, you must first set a **base case** to clarify when the function should stop. Without this condition, the function is called infinitely and the program stops. Next, we break the problem down into smaller subproblems and design a recursive step that allows the same function to solve the subproblem again. It is also important to decide whether to process the operations that need to be done at this stage first or after the recursive call. Finally, we test whether the function actually returns the desired result and then we see if it works as expected.

2. Describe the process of analyzing recursive functions. How does it differ from analyzing non-recursive functions? How is it the same?
- The recursive function analysis calculates the number of times a function is called and the number of operations per call according to the input size, and expresses the total number of operations as an ignition formula. The ignition equation is developed or solved mathematically to derive time complexity in the Big-O notation.
Similar to iterative statement-based functions, it mathematically analyzes performance based on input size. However, recursive functions overlap function calls, which require both stack memory usage and call depth to be considered, and in complex cases, optimization such as tail recursive or redundant call removal may be necessary.