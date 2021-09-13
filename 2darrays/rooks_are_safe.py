chessboard =  [[0,1,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,1] ]



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