import copy

class Car:
    def __init__(self, c, x, y):
        self.facing = c
        self.turn = 'left'
        self.x = x
        self.y = y
        self.dead = False

    def __str__(self):
        return "({}, {}) {} turning {}, dead? {}".format(self.y, self.x, self.facing, self.turn, self.dead)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)


def printTrack(track, cars):
    toPrint = copy.deepcopy(track)
    for car in cars:
        toPrint[car.x][car.y] = car.facing

    for row in toPrint:
        print(''.join(row))


def checkCollision(cars):
    for car in cars:
            for other in cars:
                if not car.dead and not other.dead:
                    if car != other and car.x == other.x and car.y == other.y:
                        print("Removing {} and {}".format(car, other))
                        car.dead = True
                        other.dead = True
                        break


def aliveCars(cars):
    numAlive = 0
    for car in cars:
        if not car.dead:
            numAlive += 1

    if numAlive % 2 == 0:
        raise Exception("Even number of cars alive, cannot end with just one!")

    if numAlive > 2:
        return True


lines = []
longest = 0
with open('input') as f:
    for line in f:
        line = line.rstrip('\n')
        lines.append(line)
        if len(line) > longest:
            longest = line
track = [[' ' for x in xrange(len(longest))] for y in xrange(len(lines))]
cars = []

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in ['>', '<', 'v', '^']:
            car = Car(c, row, col)
            cars.append(car)
            if c in ['<', '>']:
                track[row][col] = '-'
            else:
                track[row][col] = '|'
        else:
            track[row][col] = c

cars = sorted(cars)

##print("initial")
##printTrack(track, cars)

i = 0
while aliveCars(cars):
    for car in cars:
        if not car.dead:
            if car.facing == '>':
                next_track = track[car.x][car.y+1]
                if next_track == '\\':
                    #print("Forced to turn right")
                    car.facing = 'v'
                if next_track == '/':
                    #print("Forced to turn left")
                    car.facing = '^'
                elif next_track == '+':
                    if car.turn == 'left':
                        car.facing = '^'
                        car.turn = 'straight'
                        #print("Turning left at intersection, now ^")
                    elif car.turn == 'straight':
                        car.turn = 'right'
                        #print("Going straight at intersection, still >")
                    elif car.turn == 'right':
                        car.facing = 'v'
                        car.turn = 'left'
                        #print("Turning left at intersection, now v")
                #else:
                    #print("Regular track, just going")
                car.y += 1
            elif car.facing == 'v':
                next_track = track[car.x + 1][car.y]
                if next_track == '\\':
                    car.facing = '>'
                    #print("Forced to turn left")
                elif next_track == '/':
                    car.facing = '<'
                    #print("Forced to turn right")
                elif next_track == '+':
                    if car.turn == 'left':
                        car.facing = '>'
                        car.turn = 'straight'
                        #print("Turned left, now >")
                    elif car.turn == 'straight':
                        car.turn = 'right'
                        #print("Went straight, still v")
                    elif car.turn == 'right':
                        car.facing = '<'
                        car.turn = 'left'
                        #print("turned right, now <")
                #else:
                    #print("Regular track, just going")
                car.x += 1
            elif car.facing == '<':
                next_track = track[car.x][car.y-1]
                if next_track == '/':
                    #print("Forced to turn left")
                    car.facing = 'v'
                if next_track == '\\':
                    #print("Forced to turn right")
                    car.facing = '^'
                elif next_track == '+':
                    if car.turn == 'left':
                        car.facing = 'v'
                        car.turn = 'straight'
                        #print("Turning left at intersection, now v")
                    elif car.turn == 'straight':
                        car.turn = 'right'
                        #print("Going straight at intersection, still <")
                    elif car.turn == 'right':
                        car.facing = '^'
                        car.turn = 'left'
                        #print("Turning left at intersection, now ^")
                #else:
                    #print("Regular track, just going")
                car.y -= 1
            elif car.facing == '^':
                next_track = track[car.x - 1][car.y]
                if next_track == '\\':
                    car.facing = '<'
                    #print("Forced to turn left")
                elif next_track == '/':
                    car.facing = '>'
                    #print("Forced to turn right")
                elif next_track == '+':
                    if car.turn == 'left':
                        car.facing = '<'
                        car.turn = 'straight'
                        #print("Turned left, now <")
                    elif car.turn == 'straight':
                        car.turn = 'right'
                        #print("Went straight, still ^")
                    elif car.turn == 'right':
                        car.facing = '>'
                        car.turn = 'left'
                        #print("turned right, now >")
                #else:
                    #print("Regular track, just going")
                car.x -= 1
            checkCollision(cars)
    cars = sorted(cars)
    #printTrack(track, cars)
    i += 1

for car in cars:
    if not car.dead:
        print(car)
