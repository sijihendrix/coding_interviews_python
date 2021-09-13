chessboard =  [[1,0],[0,1]]



def rooks_are_safe(array):

    diagonal_sum = 0


    for i in range(len(array)):
        # diagonal_sum += array[i][i]

        print(diagonal_sum)
        if  sum(array[i]) > 1:
            return False
        # elif diagonal_sum > 1:
        #     print(False)
        #     return False       
        for j in range(len(array[i])):
            pass



rooks_are_safe(chessboard)