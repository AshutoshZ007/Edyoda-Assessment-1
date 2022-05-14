# Write a Python program that accepts a word from the user and reverse it.



# Sample Test Case



# Input : Edyoda

# output: adoydE


Magic=input("Enter word to see Magic:- ")

Rever_M=(Magic[::-1])

print(Rever_M)


Magic=input("Enter word to see Magic:- ")

for i in range((len(Magic)-1),-1,-1):
    print(Magic[i],end="")
