class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)
        start = [0,0]
        
        for move in moves:
            if move == "U":
                start[1] += 1
            elif move == "D":
                start[1] -= 1
            elif move == "R":
                start[0] += 1
            else:
                start[0] -= 1
        
        return start == [0,0]