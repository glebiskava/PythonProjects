from array import *

arr = array('i', [1,2,3,4,5]) #'i' stand for type of array elements and in the [] are the elements

#printing the array itself
print("This is the array: ", arr)

#printing every element in array
print("printing each element of array")
for i in arr:
    print(i)

#removing the 2 element of array so pop(1) bc it starts at 0
print("this is the new array without the second element")
arr.pop(1)
print(arr)

#printing every element of new popped array
print("printing each element of popped array")
for i in arr:
    print(i)c

#reversing the array
arr.reverse()
print("This is the reversed popped array: ", arr)

#adding the element 10 to the array
arr.append(10)
print("Number 10 added to the array:", arr)

#removing a specific element
#function "remove" removes always the first element which was indicated,
#so if there are two 2s it will only remove the first one
arr = array('i', [1,2,3,3,4,5,10])
print("This is the new array: ", arr)

arr.remove(3)
print("the first number 3 has beeen removed from array: ", arr) #number 3 has been removed
