class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.current = []
        index = []
        visited = set()
        def find(row , col , x):
            if self.current == list(word):
                return True
            if x >= len(word):
                return
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return 
            if board[row][col] == word[x] and (row , col) not in visited:
                self.current.append(board[row][col])
                visited.add((row,col))
                if   find(row-1, col , x+1):
                    return True
                if  find(row+1, col , x+1 ):
                    return True
                if find(row,col+1 , x+1 ):
                    return True
                if find(row,col-1 , x+1 ):
                    return True
                self.current.pop()
                visited.remove((row , col))
            # return False
        
        for i in range(0 , len(board)):
            for j in range( 0, len(board[0])):
                if board[i][j] == word[0]:
                    index.append([i , j])
    
        for i in range(len(index)):
            if find(index[i][0] , index[i][1] , 0 ):
                return True
        return False

        