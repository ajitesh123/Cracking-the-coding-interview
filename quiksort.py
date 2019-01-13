#Implmentation of Quicksort in python

def quickSort(values):
    if len(values)<=1:
        return values
    less_than_pivot=[]
    greater_than_pivot=[]
    pivot=values[0]

    for value in values[1:]:
        if value <=pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print(f"{less_than_pivot} |**| {pivot}  |**| {greater_than_pivot}")
    return quickSort(less_than_pivot)+[pivot]+quickSort(greater_than_pivot)


number=[1,8,7,9,2,3,5,6,2,4]
sorted_numbers=quickSort(number)
print(sorted_numbers)
