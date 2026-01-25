s={1,2,2,3,4,7,8,1,5,4}
#Set remove duplicate values
print(s)
print(len(s)) #length output

#to add value


#by default this is not a set 
#This is dictionaty
empty_set={}
print(type(empty_set))

#for empty set..Use constructor function
empty_set2=set()
print(type(empty_set2))

#Set method
#add
s.add(13)
print(s)

#remove
s.remove(5)
print(s)

#clear all the element from set
s.clear()
print("After Clear",s)

#Remove a random value from the set
set2={3,4,5,6,7}
set2.pop()
print("After random remove",set2)

#Set union
s1={1,2,3,4,5,6}
s2={5,6,7,8,9,10}

#union
set_union=s1.union(s2)
print(set_union)

#Intersection
set_intersection=s1.intersection(s2)
print(set_intersection)



