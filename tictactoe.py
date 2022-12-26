import random


class TicTacToe:
    def __init__(self):
        self.current_player = 0
        self.players = ["X", "O"]
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def check_winner(self, state=None):
        if state == None:
            state = self.board
        for i in range(3):
            row = [state[i][0], state[i][1], state[i][2]]
            column = [state[0][i], state[1][i], state[2][i]]
            if row == ["X", "X", "X"] or column == ["X", "X", "X"]:
                return "X"
            if row == ["O", "O", "O"] or column == ["O", "O", "O"]:
                return "O"
        diagonals = [
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if ["X", "X", "X"] in diagonals:
            return "X"
        if ["O", "O", "O"] in diagonals:
            return "O"
        for r in range(3):
            for c in range(3):
                if type(state[r][c]) == int:
                    return "N"
        return "D"

    def make_move(self, move, state=None, player=None):
        if state == None:
            state = self.board
        index = move - 1
        r = index // 3
        c = index % 3
        if state[r][c] != move:
            return "I"
        if player == None:
            player = self.current_player
            self.current_player = 1 - self.current_player
        state[r][c] = self.players[player]


def display(gamestate):
    return f"""
┏━━━┳━━━┳━━━┓
┃ {gamestate.board[0][0]} ┃ {gamestate.board[0][1]} ┃ {gamestate.board[0][2]} ┃ 
┣━━━╋━━━╋━━━┫
┃ {gamestate.board[1][0]} ┃ {gamestate.board[1][1]} ┃ {gamestate.board[1][2]} ┃
┣━━━╋━━━╋━━━┫
┃ {gamestate.board[2][0]} ┃ {gamestate.board[2][1]} ┃ {gamestate.board[2][2]} ┃
┗━━━┻━━━┻━━━┛
"""


def min_max(game_space, player_move):
    game_space = game_space[player_move]
    min_score = 10
    best_move = []
    for move in game_space:
        if type(move) is int:
            if game_space[move]["O"] < min_score:
                min_score = game_space[move]["O"]
                best_move = [move]
            if game_space[move]["O"] == min_score:
                best_move.append(move)
    resp = random.choice(best_move)
    return resp


if __name__ == "__main__":
    game = TicTacToe()
    game_space = None

    import os

    if os.path.isfile("tree.txt"):
        print("Loading game tree...")
        with open("tree.txt") as f:
            game_space = f.read()
            game_space = eval(game_space)
            print("Loaded.")

    while game.check_winner() in ["D", "N"]:
        print(display(game))
        move = int(input())
        res = game.make_move(move)
        if res != "I" and game_space:
            resp = min_max(game_space, move)
            game_space = game_space[move][resp]
            game.make_move(resp)

    print(display(game))
    print(game.check_winner())
