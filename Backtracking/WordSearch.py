from typing import List
class Solution:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def bactrack(i,j,indx):
            if indx == len(word):
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m or word[indx] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = ' '

            if bactrack(i + 1,j,indx + 1) or bactrack(i,j + 1,indx + 1) or bactrack(i - 1,j,indx + 1) or bactrack(i , j - 1, indx + 1):
                return True
            else:
                board[i][j] = temp
                return False

             

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if bactrack(i,j,0):
                        return True
        return False

if __name__ == "__main__":
    sol  = Solution()
    # Test Case 1: Word exists in the board
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word1 = "ABCCED"
    print(sol.exist(board1, word1))  # Expected output: True

    # Test Case 2: Word exists in the board in a different path
    word2 = "SEE"
    print(sol.exist(board1, word2))  # Expected output: True

    # Test Case 3: Word does not exist in the board
    word3 = "ABCB"
    print(sol.exist(board1, word3))  # Expected output: False
