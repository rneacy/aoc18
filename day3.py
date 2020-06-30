import numpy as np

with open("Inputs/3/input.txt", "r") as f:
    claims = f.read().splitlines()

grid = np.zeros((1050, 1050), dtype=int)

print_grid = False

def partA():
    for claim in claims:
        c,x,y,w,h = parse_claim(claim)

        cY = y
        cX = x

        for _ in range(w):
            for _ in range(h):
                if grid[cY, cX] == 0:
                    grid[cY, cX] = c
                else:
                    grid[cY, cX] = -1
                
                cY += 1
            cX +=1
            cY = y

    # count the overlaps
    sqm = 0
    for row in grid:
        for a in row:
            if a == -1:
                sqm += 1

    print(sqm)
    if print_grid:
        print(grid)


def parse_claim(claim: str):
    claim = claim.split("@ ")
    
    pos_data, size_data = claim[1].split(": ")
    pos_data = pos_data.split(",")
    size_data = size_data.split("x")

    x = int(pos_data[0])
    y = int(pos_data[1])

    w = int(size_data[0])
    h = int(size_data[1])

    c = int(claim[0][1:-1])

    return c,x,y,w,h

partA()