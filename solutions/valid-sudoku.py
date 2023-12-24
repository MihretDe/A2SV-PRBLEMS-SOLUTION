class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for i in range(9):
            set_num = set()
            for j in range(9):
                if board[i][j]!= "." and board[i][j] in set_num:
                    return False
                else:
                    set_num.add(board[i][j])
        
        for i in range(9):
            set_num2 = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in set_num2:
                    return False
                else:
                    set_num2.add(board[j][i])
       
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                set_num3 = set()
                list_num3 = []
                list_num3.extend(board[i][j:j+3])
                list_num3.extend(board[i+1][j:j+3])
                list_num3.extend(board[i+2][j:j+3])
                
                for num in list_num3:
                    if num != "." and num in set_num3:
                        return False
                    else:
                        set_num3.add(num)
                

        return True
