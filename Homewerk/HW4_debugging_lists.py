"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.



Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

Zero = list(range(51))

"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""

def square(Zero):
    return [x ** 2 for x in Zero]

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

combo = sorted([x for x in listA + listB if x % 2 != 0])

"""
Q3 2D Lists
Using nested for loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE
list_2D = [[5 * row + col * 2 + 1 for col in range(5)] for row in range(5)]
#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).
for row in list_2D:
    print(row)

print()



"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

for i in range(5):
    for j in range(5):
        if list_2D[i][j] % 3 == 0:
            list_2D[i][j] = '?'

for row in list_2D:
    print(row)
#What conditional can you use to check if numbers are multiples? 
    #answer: the modulo operator 

"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(a):
     return list(set(a))

#It may be helpful to create an array to test your function.
arrayer = [40, 10, 80, 50, 20, 60, 30]

result = remove_duplicates(arrayer)
print(result)