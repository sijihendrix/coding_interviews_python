arr = [32, 55, 712, 1, 890]



def second_largest(array):
    if not array:
        return None
    elif len(array) == 1:
        return None
    largest =  max(array)
    second_largest = 0
    for i in range(len(array)):
        if(array[i] > second_largest and array[i] < largest):
            second_largest = array[i]
    return second_largest


print(second_largest(arr))
            
