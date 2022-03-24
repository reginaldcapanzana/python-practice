# Given two inputs of sorted arrays
# Return one sorted array that contains elements from both inputs
# Example input: [4,6,30], [0,3,4,31]
# Expected output: [0,3,4,4,6,30,31]

def mergeSortedArrays(a, b):
    #Check if lenth of one of the inputs are 0, 
    # if so just return combined list
    if len(a) == 0 or len(b) == 0:
        return a + b

    sortedArr = []
    # Iterators
    i = 0
    j = 0

    # Compare a value from each array and append the smaller one 
    # to the sorted array. Once one array is exhausted, append
    # the remainder of the remaining array to the sorted array
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sortedArr.append(a[i])
            i += 1
        else:
            sortedArr.append(b[j])
            j += 1

    # Append the remaining list if one of the lists gets exhausted
    # a[i:] - prints elements beginning from the index to the end
    sortedArr = sortedArr + a[i:] + b[j:] 

    return sortedArr

def main():
    a = [4,6,30]
    b = [0,3,4,31]
    print(mergeSortedArrays(a,b))

if __name__ == "__main__":
    main()


                
 