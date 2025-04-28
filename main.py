import numpy as np

sample_array=np.array([2,4,6,7,8,9,10,13,16,19])

#Index Concept

print(sample_array[6]) 

#slicing operator
print(sample_array[2:5]) #from 2 to 4 but one additional due to last number is exclusive

print(sample_array[0:8]) 
print(sample_array[:8]) #Dont need to put anything for start or end if you want to print from there, just put start or end value.

print(sample_array[2:10])
print(sample_array[2:])

print(sample_array[0:10:2]) #1st=start,2nd=end,3rd=stepsize
print(sample_array[::2])

#Reversing an array

print(sample_array[::-1])

#multi-dimensional array

multi_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(multi_array[0:2,0:2]) #First is rows so 0 and 1 rows plus 1 as last number is exclusive and same for columns e.g this would be a 2x2 grid.


arr=np.arange(1,50).reshape(7,7)
print(arr)

print(arr[2:5,2:5])

arr2 = np.array([1,2,3,4,5,6,7,8,9,10])

#Printing even numbers(the module is that if divided by 2 and remainder is zero its even and if not odd)
even_array = arr2[arr2%2 == 0]
print(even_array)

odd_array = arr2[arr2%2 != 0]
print(odd_array)

#Checking if value of 5 is present in the array
a=arr2[arr2==5] #Not index value
print(a)

b=arr2[arr2==500] 
print(b)

print(arr2[[1,7,3]]) #accessesing values from index values

print(arr2[arr2<5]) #NOT INDEX VALUES
print(arr2[arr2>7]) #NOT INDEX VALUES

#Linear Equation(way to find out y from x )
def linear_eqn(x):
    y=(2*x)+3
    print(y)

x=np.array([1,2,3,4,5])

linear_eqn(x)