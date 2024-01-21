import numpy as np
from random import randint, choice
import matplotlib.pyplot as plt

qtable, Alpha, Gamma, Reward = None, 0.5, 0.75, 42.0

# The number of piles is 3

# max number of items per pile
ITEMS_MX = 10

# Initialize starting position
def init_game():
    return [randint(1, ITEMS_MX), randint(1, ITEMS_MX), randint(1, ITEMS_MX)]


# Based on X-oring the item counts in piles - mathematical solution
def nim_guru(st):
    xored = st[0] ^ st[1] ^ st[2]
    if xored == 0:
        return nim_random(st)
    #
    for pile in range(3):
        s = st[pile] ^ xored
        if s <= st[pile]:
            return st[pile] - s, pile


# Random Nim player
def nim_random(_st):
    pile = choice([i for i in range(3) if _st[i] > 0])  # find the non-empty piles
    return randint(1, _st[pile]), pile  # random move


def nim_qlearner(_st):
    # pick the best rewarding move, equation 1
    a = np.argmax(qtable[_st[0], _st[1], _st[2]])  # exploitation
    # index is based on move, pile
    move, pile = a % ITEMS_MX + 1, a // ITEMS_MX
    # check if qtable has generated a random but game illegal move - we have not explored there yet
    if move <= 0 or _st[pile] < move:
        move, pile = nim_random(_st)  # exploration

    return move, pile  # action


Engines = {'Random': nim_random, 'Guru': nim_guru, 'Qlearner': nim_qlearner}


def game(a, b):
    state, side = init_game(), 'A'
    while True:
        engine = Engines[a] if side == 'A' else Engines[b]
        move, pile = engine(state)
        # print(state, move, pile)  # debug purposes
        state[pile] -= move
        if state == [0, 0, 0]:  # game ends
            return side  # winning side

        side = 'B' if side == 'A' else 'A'  # switch sides


def play_games(_n, a, b):
    from collections import defaultdict
    wins = defaultdict(int)
    for i in range(_n):
        wins[game(a, b)] += 1
    # info
    print(f"{_n} games, {a:>8s}{wins['A']:5d}  {b:>8s}{wins['B']:5d}")

    return wins['A'], wins['B']


def game(a, b):
    state, side = init_game(), 'A'
    while True:
        engine = Engines[a] if side == 'A' else Engines[b]
        move, pile = engine(state)
        # print(state, move, pile)  # debug purposes
        state[pile] -= move
        if state == [0, 0, 0]:  # game ends
            return side  # winning side

        side = 'B' if side == 'A' else 'A'  # switch sides


def play_games(_n, a, b):
    from collections import defaultdict
    wins = defaultdict(int)
    for i in range(_n):
        wins[game(a, b)] += 1
    # info
    print(f"{_n} games, {a:>8s}{wins['A']:5d}  {b:>8s}{wins['B']:5d}")

    return wins['A'], wins['B']


# Function to print the entire set of states
def qtable_log(_fn):
    with open(_fn, 'w') as fout:
        s = 'state'
        for a in range(ITEMS_MX * 3):
            move, pile = a % ITEMS_MX + 1, a // ITEMS_MX
            s += ',%02d_%01d' % (move, pile)

        print(s, file=fout)
        for i, j, k in [(i, j, k) for i in range(ITEMS_MX + 1) for j in range(ITEMS_MX + 1) for k in
                        range(ITEMS_MX + 1)]:
            s = '%02d_%02d_%02d' % (i, j, k)
            for a in range(ITEMS_MX * 3):
                r = qtable[i, j, k, a]
                s += ',%.1f' % r

            print(s, file=fout)


# learn from _n games, randomly played to explore the possible states
def nim_qlearn(_n):
    print("nim_qlearner " + str(_n))
    global qtable
    # based on max items per pile
    qtable = np.zeros((ITEMS_MX + 1, ITEMS_MX + 1, ITEMS_MX + 1, ITEMS_MX * 3), dtype=float)

    qtable_log('qtable_debug0.txt')

    # play _n games
    for i in range(_n):
        # track all moves for the game
        movesA = []
        movesB = []
        turn = 'A'
        a, b = 'Qlearner', 'Qlearner'
        # first state is starting position
        st1 = init_game()
        while True:  # while game not finished
            engine = Engines[a] if turn == 'A' else Engines[b]
            # make a random move - exploration
            # move, pile = nim_random(st1)
            # move, pile = nim_qlearner(st1)
            move, pile = engine(st1)

            st2 = list(st1)
            # make the move
            st2[pile] -= move  # --> last move I made

            r = qtable[st2[0], st2[1], st2[2]]
            if turn == 'A':
                movesA.append((move, pile, list(st1), r))
            if turn == 'B':
                movesB.append((move, pile, list(st1), r))

            if st2 == [0, 0, 0]:  # game ends
                good_moves = movesA if turn == 'A' else movesB
                bad_moves = movesA if turn == 'B' else movesB

                # qtable_update(Reward, st1, move, pile, 0)  # I won

                for j in range(len(good_moves)):
                    stx = good_moves[j][2]
                    qtable_update(Reward, stx, good_moves[j][0], good_moves[j][1])  # I won

                for j in range(len(bad_moves)):
                    stx = bad_moves[j][2]
                    qtable_update(-Reward, stx, bad_moves[j][0], bad_moves[j][1])  # I lost

                break  # new game

            # let's just save how "good" that move was
            # qtable_update(0, st1, move, pile, np.max(qtable[st2[0], st2[1], st2[2]]))
            st1 = st2
            turn = 'B' if turn == 'A' else 'A'
    qtable_log('qtable_debug' + str(_n) + '.txt')


# Equation 3 - update the qtable
def qtable_update(r, _st1, move, pile):  # , q_future_best):
    a = pile * ITEMS_MX + move - 1
    q_future_best = qtable[_st1[0], _st1[1], _st1[2], a]
    qtable[_st1[0], _st1[1], _st1[2], a] = Alpha * (r + Gamma * q_future_best)


def plot_combined_chart(n_train, wins_list, labels, title):
    # Number of bars (groups) and the width of each bar
    n_bars = len(wins_list)
    bar_width = 0.2

    # Positions of bars on the x-axis
    r = np.arange(len(n_train))

    plt.figure(figsize=(12, 8))

    for i, (wins, label) in enumerate(zip(wins_list, labels)):
        # Calculate positions for each bar group
        positions = [x + bar_width * i for x in r]

        # Create bar plots
        plt.bar(positions, wins, width=bar_width, label=label)

        # Optional: Add line plot over bars for each series
        plt.plot(positions, wins, marker='o', linestyle='-', label=f"{label} trend")

    # Add labels, title, and legend
    plt.xlabel('Number of Training Games')
    plt.ylabel('Win Rate')
    plt.title(title)
    plt.xticks([r + bar_width for r in range(len(n_train))], n_train)
    plt.legend()

    # Show grid
    plt.grid(True)

    plt.show()


#nim_qlearn(1000)

n_train = (3, 10, 100, 1000, 10000, 5000, 100000)

wins_random = []
for n in n_train:
    nim_qlearn(n)
    a, b = play_games(10000, 'Qlearner', 'Random')
    wins_random += [a / (a + b)]

wins_guru = []
for n in n_train:
    nim_qlearn(n)
    a, b = play_games(10000, 'Qlearner', 'Guru')
    wins_guru += [a / (a + b)]


qtable_log('qtable_debug.txt')

wins_list = [wins_random, wins_guru]
labels = ["Qlearner vs Random", "Qlearner vs Guru"]

plot_combined_chart(n_train, wins_list, labels, "Qlearner Performance Comparison in Winning Starting Position")


wins_random = []
for n in n_train:
    nim_qlearn(n)
    a, b = play_games(10000, 'Random', 'Qlearner')
    wins_random += [a / (a + b)]

wins_guru = []
for n in n_train:
    nim_qlearn(n)
    a, b = play_games(10000, 'Guru', 'Qlearner')
    wins_guru += [a / (a + b)]


qtable_log('qtable_debug.txt')

wins_list = [wins_random, wins_guru]
labels = ["Random vs Qlearner", "Guru vs Qlearner"]

plot_combined_chart(n_train, wins_list, labels, "Qlearner Performance Comparison in Losing Starting Position")
