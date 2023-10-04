
#Homework 3: Data Types, Functions, Conditionals, and Loops



""" ### Problem 1: Power of a Number:
Write a function to compute the value of x raised to the power y (x^y) 
without using the built-in pow or ** operator.


"""
def pow(a,b):
    if(b==0):
        return 1     
    answer=a
    increment=a
     
    for i in range(1,b):
        for j in range (1,a):
            answer+=increment
        increment=answer
    return answer
 


"""### Problem 2: Minimum and Maximum
Write a function that takes a list of numbers as input and returns the 
minimum and maximum values in the list as a tuple.
"""



list = [(2, 3), (4, 7), (8, 11), (3, 6)]
 
print ("The original list is : " + str(list))
 
res1 = min(list)[0], max(list)[0]
res2 = min(list)[1], max(list)[1]
 

print ("The min and max of index 1 : " + str(res1))
print ("The min and max of index 2 : " + str(res2))



"""### Problem 3: Check Leap Year
Write a function that takes a year as input and returns True if it's a 
leap year, and False otherwise. A leap year is divisible by 4 but not divisible 
by 100 unless it is also divisible by 400.
"""

def leapYear(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      leap = True
  else:
      leap = False

  return leap




"""### Problem 4: Calculate BMI (Body Mass Index):
Write a function that takes a person's weight (in kilograms) and height 
(in meters) as input and returns their BMI.
"""

def calculate_bmi(weight, height):
    return round((weight / height**2),2)
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)





"""### Problem 5: Rotating Digits
Implement a function called rotate_digits that takes an integer n as input and 
rotates its digits to the right by one position. For example, given the input 12345, 
the function should return 51234. You may *not* convert the input to a string but 
you can use properties of a string in your answer.

**Hint:** Use modulus (%) and floor division (//). For example, 12345 % 10 = 5 and 
12345 // 10 = 1234
"""


def rotate_digits(digits, K):
 
   
    X = rotate_digits(digits)
 
    
    K = ((K % X) + X) % X
 
    
    left_no = digits // pow(10, X - K)

    digits = digits % pow(10, X - K)
 
    left_digit = rotate_digits(left_no)

    digits = digits * pow(10, left_digit) + left_no
    print(digits)
 

    rotate_digits(digits, K)



### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

"""Problem 6: Maximum
Given a list of numbers, find the maximum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMax(lis):
    if not lis:
        return None  # Return None for an empty list
    maxfor= lis[0]  
    maxw= lis[0]  
    
    
    for num in lis:
        if num > maxfor:
            maxfor = num
    
   
    i = 1
    while i < len(lis):
        if lis[i] > maxw:
            maxw = lis[i]
        i += 1
    
    return maxfor, maxw

list1 = [1, 3, 5, 7, 4, 6]
maxfor, maxw = findMax(list1)
print("Maximum number using for loop:", maxfor)
print("Maximum number using while loop:", maxw)




"""Problem 7: Minimum
Given a list of numbers, find the minimum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMin(lis):
    if not lis:
        return None  
    minfor = lis[0]  
    minw= lis[0]  
    
    
    for num in lis:
        if num < minfor:
            minfor = num
    
   
    i = 1
    while i > len(lis):
        if lis[i] < minw:
            minw= lis[i]
        i += 1
    
    return minfor, minw

list1 = [1, 3, 5, 7, 4, 6]
minfor, minw = findMax(list1)
print("Min with for", minfor)
print("Min with while", minw)




"""Problem 8: The Product
Given a list of numbers, calculate the product of all the numbers.
"""

def product(numList):
    if not numList:
        return None  
    product = 1
    for num in numList:
        product *= num
    return product



"""Problem 9: Vowels
Given a string, count the number of vowels in it using a for loop.

"""


def countVowels(str):
    vowel_count = 0
    
    string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
    
    
    for char in str:
        if char in string1:
            vowel_count += 1
    

    return vowel_count




"""Problem 10: Sum of Digits (Digital Root):
Given an integer, return the sum of its digits (also known as the digital 
root) For example, if the input is 12345, the output should be 15 
(1 + 2 + 3 + 4 + 5).

**Hint:** Refer to #5!

"""

# For this question, it is harder to do it as a for-loop as there is no 
# way of keeping track of all the digits.
# So, only a while-loop solution is necessary.

def sumDigits(num):

    digit_sum = 0

    while num > 0:
       
        digit = num % 10
        
        digit_sum += digit
        
        
        num = num // 10 
    
    
    return digit_sum

