# Write a Python program to:

# Create an array with the elements [1, 2, 3, 4, 5].
# Add a new element 6 at the end.
# Remove the element 3.
# Find the index of element 4.

myarr = [1,2,3,4,5]
print(myarr)
myarr.append(6)
print(myarr)
myarr.remove(3)
print(myarr)
print(myarr.index(4))

# Write a function find_max_element(arr) that takes an array as input and returns the largest element.

def find_max_element(arr):
    if not arr:
        return 'array is empty'
    largest = arr[0]
    for n in arr:
        if n > largest:
            largest = n
    return largest

myarr = [10, 4,3,2,5,3]
print(f'largest of {myarr} is {find_max_element(myarr)}')

print(f'using python max method, large element is {max(myarr)}')

