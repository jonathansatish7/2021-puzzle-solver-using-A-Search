#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: bkmaturi-josatiru-tsadey
#
# Based on skeleton code by D. Crandall, January 2021
#

import sys
import collections
from queue import PriorityQueue
import copy

ROWS = 4
COLS = 5


def printable_board(board):
    return [('%3d ') * COLS % board[j:(j + COLS)] for j in range(0, ROWS * COLS, COLS)]

# below function returns a list of possible successor states given the current state
# Here, it will give 9 possible successor states (rotate 4 rows + rotate 5 columns)
def successors(state):
    succ = []
    L1 = collections.deque(state[0:5])
    L1.rotate(-1)
    L1 = list(L1)
    for i in range(5, 20):
        L1.append(state[i])
    succ.append((L1, "L1"))

    L3 = []
    L3_1 = collections.deque(state[10:15])
    L3_1.rotate(-1)
    L3_1 = list(L3_1)
    for i in range(0, 10):
        L3.append(state[i])
    for i in range(0, 5):
        L3.append(L3_1[i])
    for i in range(15, 20):
        L3.append(state[i])
    succ.append((L3, "L3"))

    R2 = []
    R2_1 = collections.deque(state[5:10])
    R2_1.rotate()
    R2_1 = list(R2_1)
    for i in range(0, 5):
        R2.append(state[i])
    for i in range(0, 5):
        R2.append(R2_1[i])
    for i in range(10, 20):
        R2.append(state[i])
    succ.append((R2, "R2"))

    R4 = []
    R4_1 = collections.deque(state[15:20])
    R4_1.rotate()
    R4_1 = list(R4_1)
    for i in range(0, 15):
        R4.append(state[i])
    for i in range(0, 5):
        R4.append(R4_1[i])
    succ.append((R4, "R4"))

    U1 = copy.deepcopy(state)
    U1_1 = collections.deque(state[0:16:5])
    U1_1.rotate(-1)
    U1_1 = list(U1_1)
    j = 0
    for i in range(0, 16, 5):
        U1[i] = U1_1[j]
        j += 1
    succ.append((U1, "U1"))

    U3 = copy.deepcopy(state)
    U3_1 = collections.deque(state[2:18:5])
    U3_1.rotate(-1)
    U3_1 = list(U3_1)
    j = 0
    for i in range(2, 18, 5):
        U3[i] = U3_1[j]
        j += 1
    succ.append((U3, "U3"))

    U5 = copy.deepcopy(state)
    U5_1 = collections.deque(state[4:20:5])
    U5_1.rotate(-1)
    U5_1 = list(U5_1)
    j = 0
    for i in range(4, 20, 5):
        U5[i] = U5_1[j]
        j += 1
    succ.append((U5, "U5"))

    D2 = copy.deepcopy(state)
    D2_1 = collections.deque(state[1:17:5])
    D2_1.rotate()
    D2_1 = list(D2_1)
    j = 0
    for i in range(1, 17, 5):
        D2[i] = D2_1[j]
        j += 1
    succ.append((D2, "D2"))

    D4 = copy.deepcopy(state)
    D4_1 = collections.deque(state[3:19:5])
    D4_1.rotate()
    D4_1 = list(D4_1)
    j = 0
    for i in range(3, 19, 5):
        D4[i] = D4_1[j]
        j += 1
    succ.append((D4, "D4"))

    return succ


# check if we've reached the goal by comparing the each element with goal state
def is_goal(state):
    for i in range(0, len(state) - 1):
        if state[i + 1] < state[i]:
            return False
    return True

#heuristic function we are using is count of misplaced tiles. 
def misplaced_tiles(board):
    count = 0
    for i in range(0, 20):
        if board[i] != i + 1:
            count += 1
    return count

#We tried manhattan distance as heuristic, but later we realized that misplaced tiles is better heuristic than manhattan
def Manhattan_Distance(state):
    state_2D = []
    man_dist = 0
    goal_state = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    for i in range(0, len(state), 5):
        empty_list = state[i:i + 5]
        state_2D.append(empty_list)
    k = 1
    list_s = []
    while k != 21:
        for i in range(0, 4):
            for j in range(0, 5):
                if (state_2D[i][j] == k):
                    a = []
                    a.append(i)
                    a.append(j)
                    list_s.append(a)

        k = k + 1
    k = 1
    list_g = []
    while k != 21:
        for i in range(0, 4):
            for j in range(0, 5):
                if (goal_state[i][j] == k):
                    a = []
                    a.append(i)
                    a.append(j)
                    list_g.append(a)
        k = k + 1
    for i in range(len(list_g)):
        man_dist = man_dist + (abs(list_s[i][0] - list_g[i][0]) + abs(list_s[i][1] - list_g[i][1]))
    return man_dist

#Solve function 
def solve(initial_board):
    initial_board = list(initial_board)
    fringe = PriorityQueue()
    # fringe.put((Manhattan_Distance(initial_board),initial_board,[],0))
    fringe.put((0, initial_board, [], 0))
    while not fringe.empty():
        # print(fringe.qsize())
        ele = fringe.get()
        priority = ele[0]
        state_parent = ele[1]
        path_parent = ele[2]
        g = ele[3]
        g += 1
        if is_goal(state_parent):
            return path_parent

        for i in successors(state_parent):
            c = copy.deepcopy(path_parent)
            state_child = i[0]
            Direction_child = i[1]
            c.append(Direction_child)
            if is_goal(state_child):
                return c
            # pr = Manhattan_Distance(state_child)+g
            pr = misplaced_tiles(state_child) + g
            fringe.put((pr, state_child, c, g))
    return []


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise (Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [int(i) for i in line.split()]

    if len(start_state) != ROWS * COLS:
        raise (Exception("Error: couldn't parse start state file"))

    print("Start state: \n" + "\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
