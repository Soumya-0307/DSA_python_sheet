from array import *

# 1.creating an array and accessing the array
my_array=array('i',[1,2,3,44,5])
print(my_array)
for i in my_array:
    print(i)

#2.acess an individual elements through an array
print("step2")
print(my_array[3])


#3. append value to the array using append() method
print("step3")
my_array.append(6)
print(my_array)

#4.insert a value to the array using insert method
print("step4")
my_array.insert(3,44)
print(my_array)

#5 extend array using extend() method
print("step5")  
my_array1=array('i',[11,12,13])
my_array.extend(my_array1)
print(my_array)

#6 add items from list into the array usin fromlist() method
print("step6")
templist=[22,23,34]
my_array.fromlist(templist)
print(my_array)

#7 remove any array element using remove() method
print("step7")
my_array.remove(34)  #it does not check another occurancs once it finds the number, just remove the first element from the array
print(my_array)

#8. using pop() method to remove the last element
print("step8")
my_array.pop()
print(my_array)

#9. fetching any element using index method
print("step9")
print(my_array.index(22))

#10. reversing the array
print("step10")
my_array.reverse()
print(my_array)

#11.get an buffer info through nuffer_info()
print("step11")
print(my_array.buffer_info())

#12.check the no of occurance using count
print("step12")
print(my_array.count(44))

#13.coversion from  array to string using toSting() method
print("step13")
strtemp=my_array.tobytes()
print(strtemp)
ints=array('i')
ints.frombytes(strtemp)
print(ints)

#14.convert the array to list using tolits() method
print("step14")
print(my_array.tolist())

#slicing the array
print("step15")
print(my_array[1:4])



















