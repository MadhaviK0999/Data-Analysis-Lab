# List - Collection of items in box
def check_two_arrays_equal(arr1,arr2):
    return arr1 == arr2
       # print("Two given arrays are equal")
        #return arr1,arr2
    #else:
       # print("Two given arrays are not equal")
        #return arr1,arr2


print("Two given arrays are  :",check_two_arrays_equal([1,2,3,4],[1,2,3,4]))

assert check_two_arrays_equal([1,2,3,4],[1,2,3,4]) == True , "Test 6a failed"
print("Test 6a passed")


