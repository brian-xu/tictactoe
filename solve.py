from tictactoe import TicTacToe

game_space = {}

game = TicTacToe()
moves = list(range(1, 10))


def gen_games(state, moves_left, path, player):
    if game.check_winner(state) == "N":
        for i in range(len(moves_left)):
            move = moves_left[i]
            r = (move - 1) // 3
            c = (move - 1) % 3
            game.make_move(move, state, player)
            gen_games(
                state,
                moves_left[:i] + moves_left[i + 1 :],
                path + [move],
                1 - player,
            )
            state[r][c] = moves_left[i]
    else:
        temp = game_space
        for i in path:
            if i not in temp:
                temp[i] = {}
            temp = temp[i]
        temp["R"] = game.check_winner(state)


def sum_stats(space):
    if type(space) == int:
        return
    space["X"] = 0
    space["O"] = 0
    space["D"] = 0
    if "R" in space:
        space[space["R"]] += 1
        return
    else:
        for i in space:
            if type(space[i]) == dict:
                sum_stats(space[i])
                space["X"] += space[i]["X"]
                space["O"] += space[i]["O"]
                space["D"] += space[i]["D"]


def minimax(space):
    if type(space) == int:
        return
    space["X"] = 1
    space["O"] = -1
    if "R" in space:
        if space["R"] == "X":
            space["X"] = 1
            space["O"] = 1
        elif space["R"] == "D":
            space["X"] = 0
            space["O"] = 0
        elif space["R"] == "O":
            space["X"] = -1
            space["O"] = -1
    else:
        for i in space:
            if type(space[i]) == dict:
                minimax(space[i])
                space["X"] = min(space["X"], space[i]["O"])
                space["O"] = max(space["O"], space[i]["X"])


gen_games(game.board, moves, [], 0)
minimax(game_space)

f = open("tree.txt", "a")
import pprint

f.write(pprint.pformat(game_space))
f.close()
