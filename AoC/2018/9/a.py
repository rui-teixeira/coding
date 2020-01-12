from collections import deque


PLAYERS = 9 
LAST_MARBLE = 25 

players = [0] * PLAYERS
player = 1

marble = 0
current = marble
game = [current] 
index = 0

def insert(n,i,a):
    return a[:i+2] + [n] + a[i+2:]


marble += 1
while True:
    if (marble % 23) == 0:
        print "SCORE!" 
        players[player] += marble
        players[player] += game[index-6] 
        game = game[:index-6:] + game[index-5:]
        index = index - 5

    else:
        game = game[index+1:] + [marble] + game[:index+1] 
        game = game[1:] + [game[0]]
        index = (index + 2) % len(game)
        print [player+1], "{}:{}:{}".format(index, marble, game[index]), game


    player = (player + 1) % PLAYERS
    if marble < LAST_MARBLE:
        marble += 1
    else:
        break

print (
        PLAYERS, "players;",
        "last marble is worth", marble,
        "high score is", max(players)
        )
