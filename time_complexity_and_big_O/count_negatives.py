sample_arr =  [[-4,-3,-1,1],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]


def count_negatives(array):
    negative_count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < 0:
                negative_count +=1
    
    return negative_count


print(count_negatives(sample_arr))

# the above should be my O(n**2)

def count_negatives_On(array):
    count =  0
    row_i = 0
    col_i = len(array[0]) -1 # we start searching from the last element in the array
    while col_i >= 0 and row_i < len(array):
        if array[row_i][col_i] < 0:
            count += (col_i + 1) # add the position to count, obviously
            row_i += 1 # we increment row to go to the next row and search cause we do not need to search in this row cause we have seen the value less than 0
        else:
            col_i -= 1 # we decrement columns because that column doesn't contain any values less than 0
    return count

