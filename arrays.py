# creating an array


import array
import numpy as np


my_array=array.array('i',[])  #using array_module
print(my_array)
my_array1=array.array('i',[1,2,3,4])
print(my_array1)


np_array=np.array([],dtype=int)  #using numpy module
print(np_array)
np_array1=np.array([11,12,34])
print(np_array1)


#insertion of an array using array module

my_array1=array.array('i',[11,12,34,56,78])
print(my_array1)

my_array1.insert(0,10)
print(my_array1)

def traversalArray(array):
    for i in array:
        print(i)

# traversalArray(my_array1)

def acessArray(array,index):
    if(index>=len(array)):
        print("array index not present")
    else:
        print(array[index])

acessArray(my_array1,7)

     






