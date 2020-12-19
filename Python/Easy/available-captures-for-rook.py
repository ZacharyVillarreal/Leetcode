class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(8):
            for col in range(8):
                if board[row][col] == "R":
                    r = "".join(x for x in board[row] if x != ".")
                    c = "".join(board[i][col] for i in range(8) if board[i][col] != ".")
                    return sum('Rp' in i for i in (r, r[::-1], c, c[::-1]))