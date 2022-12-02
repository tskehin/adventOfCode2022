f = open("inputs/day2_input.txt", "r")
content = f.read()

move_score = {
    "Rock": 0,
    "Paper": 1,
    "Scissors": 2
}
score_move = {v: k for k, v in move_score.items()}

user_decrypt = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}
opp_decrypt = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}
strategy_decrypt = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

def get_game_score(user="", opp=""):

    if (move_score[user] - move_score[opp]) % 3 == 1:
        return 6
    if (move_score[user] - move_score[opp]) % 3 == 0:
        return 3
    else:
        return 0


def get_strategy_move(opp="", strategy=""):

    if strategy == "Win":
        return score_move[(move_score[opp] + 1) % 3]
    elif strategy == "Lose":
        return score_move[(move_score[opp] + 2) % 3]
    elif strategy == "Draw":
        return opp


rounds = [x.split(" ") for x in content.split("\n")]
scores = []

# part 1
for game in rounds:
    opp_move = opp_decrypt[game[0]]
    user_move = user_decrypt[game[1]]

    score = move_score[user_move] + 1 + get_game_score(user_move, opp_move)
    scores.append(score)

print(sum(scores))

# part 2
scores = []
for game in rounds:
    opp_move = opp_decrypt[game[0]]
    user_move = get_strategy_move(opp_move, strategy_decrypt[game[1]])

    score = move_score[user_move] + 1 + get_game_score(user_move, opp_move)
    scores.append(score)
    print(user_move, opp_move, score)

print(sum(scores))