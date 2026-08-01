class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in board]
        cols = [[] for _ in board]
        squares = [[] for _ in board]
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != ".":
                    rows[i].append(value)
                    cols[j].append(value)
                    k = ((i // 3) * 3) + j // 3
                    squares[k].append(value)
        for collection in [rows, cols, squares]:
            for vector in collection:
                print(vector)
                if len(vector) != len(set(vector)):
                    return False
        return True
        