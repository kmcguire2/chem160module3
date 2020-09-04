from random import choice

npart = 500
side = 75  #Should be an odd number
time = 0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]

for ipart in range(npart):
    # Start particle in middle of box
    x, y = side//2, side//2
    counter = 0
    while 1:
        counter += 1
        grid[x][y] = 0   #Remove particle from current spot
        # Randomly move particle
        sx, sy = choice(steps)
        x += sx
        y += sy
        # test if particle has left the box
        if x < 0 or y < 0 or x == side or y == side:
            time += counter
            break
        grid[x][y] = 1

avetime = time/npart
print("<t> = %5.2f <t>/r2=%5.2f"%(avetime, avetime/(side**2)))