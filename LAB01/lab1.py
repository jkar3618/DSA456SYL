'''
Name: Taehwa Hong
Student ID: 132546227
'''

# Function 1: wins_rock_scissors_paper
def wins_rock_scissors_paper(playerThrow, computerThrow):
    player = playerThrow.lower()
    opponent = computerThrow.lower()

    if player == opponent:
        return False

    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True

    return False

# Function 2: factorial
def factorial(n):
    if n == 0:
        return 1
    
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    
    return result


# Function 3: Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


# Function 4: sum_to_goal
def sum_to_goal(numbers, goal):
    seen = set()

    for num in numbers:
        complement = goal - num

        if complement in seen:
            return num * complement
        seen.add(num)

    return 0


# UpCounter class
class UpCounter:
    def __init__(self, step = 1):
        self.value = 0
        self.step = step

    def count(self):
        return self.value

    def update(self):
        self.value += self.step


# DownCounter class
class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step

'''
Reflection

What did you like/not like about Python
- I like learning and using Python as a new programming language. However, I usually used C++ and other languages. It makes me to be confused grammatically.

Was there anything that behaved differently than you expected in Python?
- It wasn't difficult to make 4 functions. But I was a little confused about what it meant to make a class, but I was able to solve it while studying.

Based on what you wrote in your lab, write something about the similarities and differences between Python and C/C++ and how that affects how you write your program.
- Python separates blocks by indentation, but C/C++ uses brace {}.
- Python does not require a data type declaration, but C/C++ must be a data type declaration.
- Python is fast and simple to run, but C/C++ requires compilation.

'''