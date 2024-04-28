def sorted_array():
    array = list(map(int,input("enter the space seperated values:").split()))   #applies the int() function to each substring, converting them into integers.
    n = len(array)
    res = [0]*n
    for i in range (n):
        res[i] = array[i]**2
        res.sort()
    return res

result_sorted_array = sorted_array()
print("the sorted array is :", result_sorted_array)


