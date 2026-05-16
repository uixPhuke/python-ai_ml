squares=[]

for i in range(6):
    squares.append(i**2)

print(squares)

#List Comprehension
squares=[i**2 for i in range(6)]
print(squares)

#List Comprehension with if condition
evenSquares=[i**2 for i in range(6) if i%2==0]
print(evenSquares)

#List Comprehension with if-else condition
nums=[0,-5,7,7,8,9,-2,3,4,5]

nums=[0 if i<0 else i for i in nums]
print(nums)

words=["Python","is","a","great","language"]
print(words[0].upper())

words=[val.upper() for val in words]
print(words)
