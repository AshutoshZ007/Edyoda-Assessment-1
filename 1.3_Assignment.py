# Write a Python program to count the number of even and odd numbers from a series of numbers.



# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# Expected Output :

# Number of even numbers : 5

# Number of odd numbers : 4




numbers=(1,2,3,4,5,6,7,8,9)
even_no_count=0
odd_no_count=0

for x in numbers:
    if x%2==0:
        even_no_count+=1
    else:
        odd_no_count+=1    
print("Number of even numbers :", even_no_count) 
print("Number of odd numbers :",odd_no_count)       