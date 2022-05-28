import unittest
from tictoc import TicTacGame


class TestTicTicGame(unittest.TestCase):

    def setUp(self):

        self.game = TicTacGame()

    def test_correct_input(self):

        self.game.set_pos(1, 1)
        self.assertEqual(self.game.free_pos_cnt, 8)
        self.game.set_pos(1, 2)
        self.assertEqual(self.game.free_pos_cnt, 7)
        self.game.set_pos(1, 3)
        self.assertEqual(self.game.free_pos_cnt, 6)
        self.game.set_pos(2, 1)
        self.assertEqual(self.game.free_pos_cnt, 5)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.free_pos_cnt, 4)
        self.game.set_pos(2, 3)
        self.assertEqual(self.game.free_pos_cnt, 3)
        self.game.set_pos(3, 1)
        self.assertEqual(self.game.free_pos_cnt, 2)
        self.game.set_pos(3, 2)
        self.assertEqual(self.game.free_pos_cnt, 1)
        self.game.set_pos(3, 3)
        self.assertEqual(self.game.free_pos_cnt, 0)

        self.assertEqual(self.game.board[0][0], 1)
        self.assertEqual(self.game.board[0][1], 1)
        self.assertEqual(self.game.board[0][2], 1)
        self.assertEqual(self.game.board[1][0], 1)
        self.assertEqual(self.game.board[1][1], 1)
        self.assertEqual(self.game.board[1][2], 1)
        self.assertEqual(self.game.board[2][0], 1)
        self.assertEqual(self.game.board[2][1], 1)
        self.assertEqual(self.game.board[2][2], 1)

    def test_incorrect_input(self):

        self.assertEqual(self.game.validate_input(1.1, 1), False)
        self.assertEqual(self.game.validate_input(1, 2.2), False)
        self.assertEqual(self.game.validate_input(3.3, 4.4), False)
        self.assertEqual(self.game.validate_input(0, 2), False)
        self.assertEqual(self.game.validate_input(1, -1), False)
        self.assertEqual(self.game.validate_input(-2, -2), False)
        self.assertEqual(self.game.validate_input(4, 3), False)
        self.assertEqual(self.game.validate_input(2, 5), False)
        self.assertEqual(self.game.validate_input(6, 7), False)
        with self.assertRaises(ValueError):
            self.assertEqual(self.game.validate_input('a', 1), False)
        with self.assertRaises(ValueError):
            self.assertEqual(self.game.validate_input(2, 'b'), False)
        with self.assertRaises(ValueError):
            self.assertEqual(self.game.validate_input('c', 'd'), False)

    def test_busy_fields(self):

        self.game.set_pos(1, 1)
        self.assertEqual(self.game.validate_input(1, 1), False)
        self.assertEqual(self.game.free_pos_cnt, 8)
        self.game.set_pos(1, 2)
        self.assertEqual(self.game.validate_input(1, 2), False)
        self.assertEqual(self.game.free_pos_cnt, 7)
        self.game.set_pos(1, 3)
        self.assertEqual(self.game.validate_input(1, 3), False)
        self.assertEqual(self.game.free_pos_cnt, 6)
        self.game.set_pos(2, 1)
        self.assertEqual(self.game.validate_input(2, 1), False)
        self.assertEqual(self.game.free_pos_cnt, 5)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.validate_input(2, 2), False)
        self.assertEqual(self.game.free_pos_cnt, 4)
        self.game.set_pos(2, 3)
        self.assertEqual(self.game.validate_input(2, 3), False)
        self.assertEqual(self.game.free_pos_cnt, 3)
        self.game.set_pos(3, 1)
        self.assertEqual(self.game.validate_input(3, 1), False)
        self.assertEqual(self.game.free_pos_cnt, 2)
        self.game.set_pos(3, 2)
        self.assertEqual(self.game.validate_input(3, 2), False)
        self.assertEqual(self.game.free_pos_cnt, 1)
        self.game.set_pos(3, 3)
        self.assertEqual(self.game.validate_input(3, 3), False)
        self.assertEqual(self.game.free_pos_cnt, 0)

    def test_player_won_first_row(self):

        self.game.set_pos(1, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(1, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(1, 3)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_second_row(self):

        self.game.set_pos(2, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 3)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_third_row(self):

        self.game.set_pos(3, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 3)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_first_column(self):

        self.game.set_pos(1, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 1)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_second_column(self):

        self.game.set_pos(1, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 2)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_third_column(self):

        self.game.set_pos(1, 3)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 3)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 3)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_first_diagonal(self):

        self.game.set_pos(1, 1)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 3)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_player_won_second_diagonal(self):

        self.game.set_pos(1, 3)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(2, 2)
        self.assertEqual(self.game.check_winner(), -1)
        self.game.set_pos(3, 1)
        self.game.show_board()
        self.assertEqual(self.game.check_winner(), 1)

    def test_draw(self):

        self.game.board[0][0] = 1
        self.game.board[1][1] = 2
        self.game.board[1][0] = 1
        self.game.board[2][0] = 2
        self.game.board[0][2] = 1
        self.game.board[0][1] = 2
        self.game.board[2][1] = 1
        self.game.board[1][2] = 2
        self.game.board[2][2] = 1
        self.game.free_pos_cnt = 0
        self.game.show_board()

        self.assertEqual(self.game.check_winner(), 0)


if __name__ == '__main__':
    unittest.main()
