#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

print("Winner: {}".format(isWinner(50, [92, 15, 31, 74, 53])))

print("Winner: {}".format(isWinner(13, [11, 57, 19, 41, 37])))
