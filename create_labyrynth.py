import random
import time
from colorama import init
from colorama import Fore, Back, Style

labyrynth = []

def printLabyrynth():
    rst = ""
    labyrynth[1][1] = "c"
    for i in range(0, width):
        if (labyrynth[height - 1][i] == 'c'):
            labyrynth[height - 1][i] = 'E'
    for i in range(0, height):
        for j in range(0, width):
            end = ""
            if (j == width - 1):
                end = '\n'
            rst += str(labyrynth[i][j]) + end
    return labyrynth



def encompassingCells(rand_Divider):
    s_cells = 0
    if (labyrynth[rand_Divider[0] - 1][rand_Divider[1]] == 'c'):
        s_cells += 1
    if (labyrynth[rand_Divider[0] + 1][rand_Divider[1]] == 'c'):
        s_cells += 1
    if (labyrynth[rand_Divider[0]][rand_Divider[1] - 1] == 'c'):
        s_cells += 1
    if (labyrynth[rand_Divider[0]][rand_Divider[1] + 1] == 'c'):
        s_cells += 1

    return s_cells


## Main code
# Init variables
divider = 'w'
cell = 'c'
unvisited = 'u'
print('Please choose level:')
print('1. Easy')
print('2. Normal')
print('3. Hard')
print('Enter a number of level')
level = input()
height = 18
width = 27
if (level == '1'):
    height = 10
    width = 15
elif(level == '2'):
    height = 15
    width = 20
print('Please open window with python icon to start play')
# Initialize colorama
init()

# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    labyrynth.append(line)

# Randomize starting point and set it a cell
beginning_height = int(random.random() * height)
beginning_width = int(random.random() * width)
if (beginning_height == 0):
    beginning_height += 1
if (beginning_height == height - 1):
    beginning_height -= 1
if (beginning_width == 0):
    beginning_width += 1
if (beginning_width == width - 1):
    beginning_width -= 1

# Mark it as cell and add surrounding Dividers to the list
labyrynth[beginning_height][beginning_width] = cell
dividers = []
dividers.append([beginning_height - 1, beginning_width])
dividers.append([beginning_height, beginning_width - 1])
dividers.append([beginning_height, beginning_width + 1])
dividers.append([beginning_height + 1, beginning_width])

# Denote Dividers in maze
labyrynth[beginning_height - 1][beginning_width] = 'w'
labyrynth[beginning_height][beginning_width - 1] = 'w'
labyrynth[beginning_height][beginning_width + 1] = 'w'
labyrynth[beginning_height + 1][beginning_width] = 'w'

while (dividers):
    # Pick a random Divider
    rand_divider = dividers[int(random.random() * len(dividers)) - 1]

    # Check if it is a left Divider
    if (rand_divider[1] != 0):
        if (labyrynth[rand_divider[0]][rand_divider[1] - 1] == 'u' and labyrynth[rand_divider[0]][rand_divider[1] + 1] == 'c'):
            # Find the number of encompassing cells
            encompassing_cells = encompassingCells(rand_divider)

            if (encompassing_cells < 2):
                # Denote the new path
                labyrynth[rand_divider[0]][rand_divider[1]] = 'c'

                # Mark the new Dividers
                # Upper cell
                if (rand_divider[0] != 0):
                    if (labyrynth[rand_divider[0] - 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] - 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] - 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] - 1, rand_divider[1]])

                # Bottom cell
                if (rand_divider[0] != height - 1):
                    if (labyrynth[rand_divider[0] + 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] + 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] + 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] + 1, rand_divider[1]])

                # Leftmost cell
                if (rand_divider[1] != 0):
                    if (labyrynth[rand_divider[0]][rand_divider[1] - 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] - 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] - 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] - 1])

            # Delete Divider
            for divider in dividers:
                if (divider[0] == rand_divider[0] and divider[1] == rand_divider[1]):
                    dividers.remove(divider)

            continue

    # Check if it is an upper Divider
    if (rand_divider[0] != 0):
        if (labyrynth[rand_divider[0] - 1][rand_divider[1]] == 'u' and labyrynth[rand_divider[0] + 1][rand_divider[1]] == 'c'):

            encompassing_cells = encompassingCells(rand_divider)
            if (encompassing_cells < 2):
                # Denote the new path
                labyrynth[rand_divider[0]][rand_divider[1]] = 'c'

                # Mark the new Dividers
                # Upper cell
                if (rand_divider[0] != 0):
                    if (labyrynth[rand_divider[0] - 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] - 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] - 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] - 1, rand_divider[1]])

                # Leftmost cell
                if (rand_divider[1] != 0):
                    if (labyrynth[rand_divider[0]][rand_divider[1] - 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] - 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] - 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] - 1])

                # Rightmost cell
                if (rand_divider[1] != width - 1):
                    if (labyrynth[rand_divider[0]][rand_divider[1] + 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] + 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] + 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] + 1])

            # Delete Divider
            for divider in dividers:
                if (divider[0] == rand_divider[0] and divider[1] == rand_divider[1]):
                    dividers.remove(divider)

            continue

    # Check the bottom Divider
    if (rand_divider[0] != height - 1):
        if (labyrynth[rand_divider[0] + 1][rand_divider[1]] == 'u' and labyrynth[rand_divider[0] - 1][rand_divider[1]] == 'c'):

            encompassing_cells = encompassingCells(rand_divider)
            if (encompassing_cells < 2):
                # Denote the new path
                labyrynth[rand_divider[0]][rand_divider[1]] = 'c'

                # Mark the new Dividers
                if (rand_divider[0] != height - 1):
                    if (labyrynth[rand_divider[0] + 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] + 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] + 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] + 1, rand_divider[1]])
                if (rand_divider[1] != 0):
                    if (labyrynth[rand_divider[0]][rand_divider[1] - 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] - 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] - 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] - 1])
                if (rand_divider[1] != width - 1):
                    if (labyrynth[rand_divider[0]][rand_divider[1] + 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] + 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] + 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] + 1])

            # Delete Divider
            for divider in dividers:
                if (divider[0] == rand_divider[0] and divider[1] == rand_divider[1]):
                    dividers.remove(divider)

            continue

    # Check the right Divider
    if (rand_divider[1] != width - 1):
        if (labyrynth[rand_divider[0]][rand_divider[1] + 1] == 'u' and labyrynth[rand_divider[0]][rand_divider[1] - 1] == 'c'):

            encompassing_cells = encompassingCells(rand_divider)
            if (encompassing_cells < 2):
                # Denote the new path
                labyrynth[rand_divider[0]][rand_divider[1]] = 'c'

                # Mark the new Dividers
                if (rand_divider[1] != width - 1):
                    if (labyrynth[rand_divider[0]][rand_divider[1] + 1] != 'c'):
                        labyrynth[rand_divider[0]][rand_divider[1] + 1] = 'w'
                    if ([rand_divider[0], rand_divider[1] + 1] not in dividers):
                        dividers.append([rand_divider[0], rand_divider[1] + 1])
                if (rand_divider[0] != height - 1):
                    if (labyrynth[rand_divider[0] + 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] + 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] + 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] + 1, rand_divider[1]])
                if (rand_divider[0] != 0):
                    if (labyrynth[rand_divider[0] - 1][rand_divider[1]] != 'c'):
                        labyrynth[rand_divider[0] - 1][rand_divider[1]] = 'w'
                    if ([rand_divider[0] - 1, rand_divider[1]] not in dividers):
                        dividers.append([rand_divider[0] - 1, rand_divider[1]])

            # Delete Divider
            for divider in dividers:
                if (divider[0] == rand_divider[0] and divider[1] == rand_divider[1]):
                    dividers.remove(divider)

            continue

    # Delete the Divider from the list anyway
    for divider in dividers:
        if (divider[0] == rand_divider[0] and divider[1] == rand_divider[1]):
            dividers.remove(divider)

# Mark the remaining unvisited cells as Dividers
for i in range(0, height):
    for j in range(0, width):
        if (labyrynth[i][j] == 'u'):
            labyrynth[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
    if (labyrynth[1][i] == 'c'):
        labyrynth[0][i] = 'c'
        break

for i in range(width - 1, 0, -1):
    if (labyrynth[height - 2][i] == 'c'):
        labyrynth[height - 1][i] = 'c'
        break

# Print final maze