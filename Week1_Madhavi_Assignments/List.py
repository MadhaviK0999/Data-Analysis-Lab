# List - Collection of items in box
#HW 4 Example: Finding the length of the array without using len()
def array_length(arr):
    count=0
    for i in arr:
       count=+1
    return count
print("Length of the array : " ,array_length([]))

#more examples : return the length of the array
def array_length(arr):
    count=0  #start from 0
    for i in arr: # go through each item
        count+=1 # add 1 each time
    return count #give final count
print("Length of the array :" , array_length([5,6,7,8]))
assert array_length([5,6,7,8])==4, "Test 4a failed"
print("Test 4a passed")
assert array_length([2])==1, "Test 4b failed"
print("Test 4b passed")

#HW 5 Example: Returns a list of only odd numbers from the given list.
#HW 4 Example: Finding the length of the array without using len()
def get_odd_numbers(numbers):
    odd_numbers=[]
    for n in numbers:
        if n%2==1:
         odd_numbers.append(n)
    return odd_numbers
print("Odd Numbers : " ,get_odd_numbers([2,3,5,6,8,9,4,11,10]) )
assert get_odd_numbers([2,3,5,6,8,9,4,11,10])==[3,5,9,11], "Test 5a failed"
print("Test 5a passed")

# HW6 Example: Return true if two given lists are equal othewise return false.
def check_two_arrays_equal(arr1,arr2):
    return arr1 == arr2
       # print("Two given arrays are equal")
        #return arr1,arr2
    #else:
       # print("Two given arrays are not equal")
        #return arr1,arr2


print("Two given arrays are  :",check_two_arrays_equal([1,2,3,4],[1,2,3,4]))

assert check_two_arrays_equal([1,2,3,4],[1,2,3,4]) == True , "Test 6a failed" #checking if the function is correct or not,if it is correct it returns true and if it is not correct it will through an assertion error
print("Test 6a passed")
