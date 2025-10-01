#------------import libraries------------#
import sys                                  # import sys to use sys functions
import random                               # import random to use random functions
import pygame as py                         # import pygame to use pygame functions
import time                                 # import time to use time functions

#---------main function---------#
def main(n,sortingType):

    startingTime = time.time()

    #print(f"Sorting type {sortingType}")

    #---------create a shuffled list---------#
    numbers = createShuffledList()

    #---------init pygame---------#
    py.init()                                               # init pygame
    width = 1280                                             # set screen width and height
    height = 720
    screen = py.display.set_mode((width, height))           # create screen
    py.display.set_caption("Sorting Algorithm 1")           # set caption from the screen
    running = True

    sortingStarted = False
    sortingFinished = False
    sortedNumbers = []
    #sortedNumbers = bubbleSort(numbers)

    sleepTime = 0
    #----------------select sorting algorithm----------------#
    match sortingType:
        case 1:
            sortedNumbers = bubbleSort(numbers)
            print("Using bubble sort.")
        case 2:
            sortedNumbers = selectionSort(numbers)
            print("Using selection sort.")
        case 3:
            sortedNumbers = insertionSort(numbers)
            print("Using Insertion sort.")
        case 4:
            sortedNumbers = mergeSort(numbers)
            print("Using Merge sort.")
        case 5:
            sortedNumbers = quickSort(numbers)
            print("Using Quick sort.")
        case 6:
            sortedNumbers = heapSort(numbers)
            print("Using Heap sort.")
        case 7:
            sortedNumbers = countingSort(numbers)
            print("Using Counting sort.")
        case 8:
            sortedNumbers = shellSort(numbers)
            print("Using Shell sort.")
        case 9:
            sortedNumbers = timSort(numbers)
            print("Using Tim sort.")
        case 10:
            sortedNumbers = radixSort(numbers)
            print("Using Radix sort.")
        case 11:
            sortedNumbers = stalinSort(numbers)
            print("Using Stalin sort.")

    #-----------main loop------------#
    while running:                                          # main loop checks whether the window is still open
        for event in py.event.get():                        # and will update everything
            if event.type == py.QUIT:
                running = False
            keys = py.key.get_pressed()
            if keys[py.K_SPACE]:
                sortingStarted = True
                startingTime = time.time()

        screen.fill((0, 0, 0))                              # background is black

        drawRects(screen, numbers, width, height)           # draw bars

        if sortingStarted and not sortingFinished:                      # ChatGPT:
            try:                                                        # try:
                next(sortedNumbers)                                     #   next()
            except StopIteration:                                       # except StopIteration
                endingTime = time.time()
                print(f"Total time: {round((endingTime - startingTime), 4)}s")
                sortingFinished = True

        time.sleep(sleepTime)
        py.display.update()



    py.quit()

#----------function to draw rects-------------#
def drawRects(screen, lst, width, height):
    bar_width = width / len(lst)                            # every bar has the same width
    max_value = max(lst)                                    # highest value in the list
    green = (0, 0, 0)

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

def selectionSort(lst):

    n = len(lst)
    for i in range(n):
        smallestIndex = i
        for j in range(i + 1, n):
            if lst[j] < lst[smallestIndex]:
                smallestIndex = j
        if smallestIndex != i:
            lst[i], lst[smallestIndex] = lst[smallestIndex], lst[i]
            yield lst

def insertionSort(lst):
    pass

def mergeSort(lst):
    pass

def quickSort(lst):
    pass

def heapSort(lst):
    pass

def countingSort(lst):
    pass

def shellSort(lst):
    pass

def timSort(lst):
    pass

def radixSort(lst):
    pass

def stalinSort(lst):
    pass

if __name__ == "__main__":

    n = int(sys.argv[1])
    sortingType = int(sys.argv[2])
    main(n, sortingType)


# youtube video: https://www.youtube.com/watch?v=rbbTd-gkajw
