'''
Name: Taehwa Hong
Student ID: 132546227
'''

# Function 1
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Function 2
def linear_search(list, key):
    def helper(index):
        if index >= len(list):
            return -1
        if list[index] == key:
            return index
        return helper(index + 1)
    return helper(0)

# Function 3
def binary_search(list, key):
    def helper(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)
    return helper(0, len(list) - 1)
