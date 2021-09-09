arr = [-1, -2, -4, 5, 4,5]


#ToDo: Account for situation where there are two elements with the largest value

def second_largest(array):
    if not array:
        return None
    elif len(array) == 1:
        return None
    largest =  max(array)
    second_largest = min(array)
    for i in range(len(array)):
        if(array[i] > second_largest and array[i] != largest):
            second_largest = array[i]
    return second_largest


print(second_largest(arr))
            


def second_largest_sol(array):
    largest = None
    second_largest =  None
    for current_number in array:
        if largest == None:
            largest =  current_number
        elif current_number > largest:
            second_largest = largest
            largest = current_number
        elif second_largest == None:
            second_largest = current_number
        elif current_number > second_largest:
            second_largest = current_number
    return second_largest

   
print(second_largest_sol(arr))



def second_largest_geeks(list1):

    mx=max(list1[0],list1[1])
    secondmax=min(list1[0],list1[1])
    n =len(list1)
    for i in range(2,n):
        if list1[i]>mx:
            secondmax=mx
            mx=list1[i]
        elif list1[i]>secondmax and \
            mx != list1[i]:
            secondmax=list1[i]
    
    print("Second highest number is : ",\
        str(secondmax))


print(second_largest_geeks(arr))


def second_largest_ON(array):

    array.sort()

    return array[-2]


print(second_largest_ON(arr))

 