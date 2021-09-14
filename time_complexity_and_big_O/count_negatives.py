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


