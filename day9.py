import collections

with open("Inputs/9/input.txt", "r") as f:
    inp = f.readline()
    players = int(inp.split(" ")[0])
    l_marble = int(inp.split("worth ")[1].split(" ")[0])

marbles = collections.deque()
player_scores = {x: 0 for x in range(players)}

def partA():
    i = 0
    c_marble = 1

    marbles.append(0) # first marble

    while c_marble < l_marble:
        for player in range(players): # place marbles
            #print(marbles)
            if c_marble % 23 == 0:
                player_scores[player] += c_marble
                i = ((i - 7) % len(marbles))
                player_scores[player] += marbles[i]
                del marbles[i]
                #c_marble = marbles[i]
                c_marble += 1
                continue

            if len(marbles) != 1:
                i = ((i + 2) % len(marbles))
            else:
                i = 1
            marbles.insert(i, c_marble)
            c_marble += 1

    print(max(player_scores.values()))

try:
    partA()
except KeyboardInterrupt:
    print("done")