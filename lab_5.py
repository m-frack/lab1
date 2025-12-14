class Board:
    def __init__(self, n = 8):
        self.n = n
        self.queens = []

    def place(self, row, col):
        self.queens.append((row, col))

    def remove(self, row, col):
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        for r, c in self.queens:
            if c == col: return False
            if r == row: return False
            if abs(r - row) == abs(c - col): return False
        return True

    def solve(self, row = 0):
        if row == self.n:
            # print(self)
            # print()
            # ^drukowanie plansz z rozwiazaniami
            return 1

        count = 0
        for col in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                count += self.solve(row + 1)
                self.remove(row, col)
        return count

    def __str__(self):
        board = [["_" for _ in range(self.n)] for _ in range(self.n)]
        for r, c in self.queens:
            board[r][c] = "X"
        return "\n".join(" ".join(row) for row in board)

    def __repr__(self):
        return f"Board(n = {self.n}, queens = {self.queens})"

    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        yield from self.queens

    def __contains__(self, pos):
        return pos in self.queens

def solve(n = 8):
    return Board(n).solve()

def main():
    print(solve(1))
    print(solve(2))
    print(solve(3))
    print(solve(4))
    print(solve(8))

if __name__ == "__main__":
    main()