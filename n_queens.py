class NQBacktracking:
    def __init__(self, x_, y_):
        self.ld = [0] * 30
        self.rd = [0] * 30
        self.cl = [0] * 30
        self.x = x_
        self.y = y_

    def printSolution(self, board):
        print("N Queen Backtracking Solution:\nGiven initial position of 1st queen at row:", self.x, "column:", self.y, "\n")
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        if col >= N:
            return True
        if col == self.y:
            return self.solveNQUtil(board, col + 1)
        for i in range(N):
            if i == self.x:
                continue
            if (self.ld[i - col + N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1
                if self.solveNQUtil(board, col + 1):
                    return True
                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0
        return False

    def solveNQ(self):
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1
        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard: "))
    x = int(input("Enter the row for the first queen: "))
    y = int(input("Enter the column for the first queen: "))

    if N <= 0 or x < 0 or y < 0 or x >= N or y >= N:
        print("Invalid input. Please enter valid values.")
    else:
        NQBt = NQBacktracking(x, y)
        NQBt.solveNQ()
