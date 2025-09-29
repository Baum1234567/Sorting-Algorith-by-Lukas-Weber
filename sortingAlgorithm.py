#------------import libraries------------#
import sys                                  # import sys to use sys functions
import random                               # import random to use random functions
import pygame as py                         # import pygame to use pygame functions
import time                                 # import time to use time functions

#---------main function---------#
def main(n,sortingType):

    print(f"Sorting type {sortingType}")

    #---------create a shuffled list---------#
    numbers = createShuffledList()

    #---------init pygame---------#
    py.init()                                               # init pygame
    width = 1280                                             # set screen width and height
    height = 720
    screen = py.display.set_mode((width, height))           # create screen
    py.display.set_caption("Sorting Algorithm 1")           # set caption from the screen
    running = True

    sortedNumbers = []
    #sortedNumbers = bubbleSort(numbers)

    sleepTime = 0
    #----------------select sorting algorithm----------------#
    match sortingType:
        case 1:
            sortedNumbers = bubbleSort(numbers)
            print("Using bubble sort.")
        case 2:
            sortedNumbers = cocktailSort(numbers)
            print("Using Cocktail sort.")
        case 3:
            sortedNumbers = insertionSort(numbers)
            print("Using Insertion sort.")
        case 4:
            sortedNumbers = selectionSort(numbers)
            print("Using Selection sort.")
            sleepTime = 0.05

    #-----------main loop------------#
    while running:                                          # main loop checks whether the window is still open
        for event in py.event.get():                        # and will update everything
            if event.type == py.QUIT:
                running = False
        screen.fill((0, 0, 0))                              # background is black

        drawRects(screen, numbers, width, height)           # draw bars

        try:                                                # credits to ChatGPT: without those 4 lines
            next(sortedNumbers)                             # there would be no animation,
        except StopIteration:                               # it would be sorted all at once, and
            pass                                            # you wouldn't see how the algorithm works

        time.sleep(sleepTime)
        py.display.update()

    py.quit()

#----------function to draw rects-------------#
def drawRects(screen, lst, width, height):
    bar_width = width / len(lst)                            # every bar has the same width
    max_value = max(lst)                                    # highest value in the list
    green = (0, 255, 0)

    for i, val in enumerate(lst):
        bar_height = int((val / max_value) * height)
        x = i * bar_width
        y = height - bar_height
        py.draw.rect(screen, green, (x, y, bar_width, bar_height))

#----------function to create a shuffled list-------------#
def createShuffledList():
    i = 1
    numbersToSort = []
    for x in range(1, n + 1):

        numbersToSort.append(i)
        i += 1

    #print(numbersToSort)
    shuffledNumbers = shuffel(numbersToSort)
    #print(shuffledNumbers)
    return shuffledNumbers

#----------function to shuffle a list-------------#
def shuffel(lst):
    shuffledNumbers = lst.copy()                        # original list has to be copied in order to shuffle it
    random.shuffle(shuffledNumbers)                     # the copied list is shuffled
    return shuffledNumbers                              # the shuffled list is returned


#--------------buble sort--------------#
def bubbleSort(lst):

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                yield lst

def cocktailSort(lst):
    n = len(lst)
    start = 0
    end = n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                yield lst
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                yield lst
        start += 1

def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
            yield lst
        lst[j + 1] = key
        yield lst


def selectionSort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            yield lst




if __name__ == "__main__":

    n = int(sys.argv[1])
    sortingType = int(sys.argv[2])
    main(n, sortingType)

