class TicTacGame:

    def __init__(self):

        self.board = [[0] * 3 for i in range(3)]
        self.free_pos_cnt = 9
        self.cur_gamer = 1

    def show_board(self):

        print()
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()
        print()

    def validate_input(self, x, y):

        if (x != int(x)) or (x < 1) or (x > 3):
            return False

        if (y != int(y)) or (y < 1) or (y > 3):
            return False

        return self.board[x - 1][y - 1] == 0

    def set_pos(self, x, y):

        self.board[x - 1][y - 1] = self.cur_gamer
        self.free_pos_cnt -= 1

    def start_game(self):

        while True:

            print('Player 1, your turn:')
            self.cur_gamer = 1

            x, y = map(int, input().split())

            while not self.validate_input(x, y):
                print('The position is incorrect or busy. Try again.')
                x, y = map(int, input().split())

            self.set_pos(x, y)

            self.show_board()

            res = self.check_winner()
            print(res)

            if res < 0:

                print('Player 2, your turn:')
                self.cur_gamer = 2

                x, y = map(int, input().split())
                while not self.validate_input(x, y):
                    print('The position is busy. Try again.')
                    x, y = map(int, input().split())

                self.set_pos(x, y)

                self.show_board()

                res = self.check_winner()
                print(res)

                if res < 0:
                    continue

            if res > 0:
                print("Game over: player", str(self.cur_gamer), "won")
            else:
                print("Game over: draw")

            break

    def check_winner(self):

        def check_rows():

            for i in range(3):

                if len(set(self.board[i])) == 1:

                    if self.board[i][0] > 0:
                        return True

            return False

        def check_columns():

            for i in range(3):

                if len(set([self.board[0][i], self.board[1][i], self.board[2][i]])) == 1:

                    if self.board[0][i] > 0:
                        return True

            return False

        def check_diagonals():

            if len(set([self.board[0][0], self.board[1][1], self.board[2][2]])) == 1:

                if self.board[0][0] > 0:
                    return True

            if len(set([self.board[0][2], self.board[1][1], self.board[2][0]])) == 1:
                if self.board[0][2] > 0:
                    return True

            return False

        res = check_rows()
        if not res:
            res = check_columns()
            if not res:
                res = check_diagonals()

        if res:
            return 1  # есть победитель
        elif self.free_pos_cnt > 0:
            return -1  # игра продолжается
        else:
            return 0  # ничья


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
