chessboard = [[1]]


#  [[0,1,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,1] ]



def rooks_are_safe(array):

    for i in range(len(array)):
        if  sum(array[i]) > 1:
            return False    
        for j in range(len(array[i])):  
            res = [sub[j] for sub in array]
            if  sum(res) > 1:
                return False
        
    return True

print(rooks_are_safe(chessboard))

def rooks_are_safe2(chessboard):
    n = len(chessboard)

    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
        if row_count > 1:
            return False 
    
    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col_i]
        if col_count > 1:
            return False
    
    return True

# Instucture's code above. Totally prefer mine rooks_are_safe()
print(rooks_are_safe2(chessboard))