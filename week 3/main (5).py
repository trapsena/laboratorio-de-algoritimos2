def robb(matrix):
    n = len(matrix)
    bigger = 0
    
    for line in range(n):
        side = 1
        horiz = 1
        for colune in range(n):
            side *= matrix[line][colune]
            horiz *= matrix[colune][line]
        
        if side > bigger:
            bigger = side   
        if horiz > bigger:
            bigger = horiz
    

    diag = 1
    rev_diag = 1
    
    for i in range(n):
        diag *= matrix[i][i]
        rev_diag *= matrix[i][n - i - 1]    
    if rev_diag > diag:
        diag = rev_diag    
    if diag > bigger:
        bigger = diag


    return bigger



def main():
    matrix = [[8, 2,  3, 9, 1],
              [5, 2, 3,  6,  8],
              [4, 2,  1, 6, 2],
              [5, 3, 3,  9, 1],
              [ 9, 10, 2, 8, 5]]
              
    bigger = robb(matrix)
    print(bigger)

main()