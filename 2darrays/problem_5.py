two_d_array = [[1,2,3], [4,5,6], [7,8,9]]

array_2 = [[1, 0],[0, 1]]

def diagonal_sum(two_d_array):
    sum = 0
    for i in range(len(two_d_array)):
        for j in range(len(two_d_array[i])):
            if i == j:
                sum += two_d_array[i][j]

    return sum

print(diagonal_sum(array_2))


def diagonal_sum_0n(two_d_array):
    total = 0
    for i in range(len(two_d_array)):
        total += two_d_array[i][i]