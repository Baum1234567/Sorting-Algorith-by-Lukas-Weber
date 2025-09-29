#------------import libraries------------#
import sys                                  # import sys to use sys functions
import random                               # import random to use random functions
import pygame as py                         # import pygame to use pygame functions

#---------main function---------#
def main(n):

    #---------create a shuffled list---------#
    createShuffledList()

    #---------init pygame---------#
    py.init()                                               # init pygame
    width = 700                                             # set screen width and height
    height = 400
    screen = py.display.set_mode((width, height))           # create screen
    py.display.set_caption("Sorting Algorithm 1")           # set caption from the screen
    running = True

    #-----------main loop------------#
    while running:                                          # main loop checks whether the window is still open
        for event in py.event.get():                        # and will update everything
            if event.type == py.QUIT:
                running = False
        screen.fill((0, 0, 0))
        py.display.update()
    py.quit()

#----------function to draw rects-------------#
def drawRects(lst):

    for nums in lst:
        py.rect

#----------function to create a shuffled list-------------#
def createShuffledList():
    i = 1
    numbersToSort = []
    for x in range(1, n + 1):

        numbersToSort.append(i)
        i += 1

    print(numbersToSort)
    shuffledNumbers = shuffel(numbersToSort)
    print(shuffledNumbers)

#----------function to shuffle a list-------------#
def shuffel(lst):
    shuffledNumbers = lst.copy()                        # original list has to be copied in order to shuffle it
    random.shuffle(shuffledNumbers)                     # the copied list is shuffled
    return shuffledNumbers                              # the shuffled list is returned


if __name__ == "__main__":

    n = int(sys.argv[1])
    main(n)

