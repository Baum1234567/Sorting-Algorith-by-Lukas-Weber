#------------import libraries------------#
import sys                                  # import sys to use sys functions
import random                               # import random to use random functions
import pygame as py                         # import pygame to use pygame functions
import time                                 # import time to use time functions

#---------main function---------#
def main(n):

    #---------create a shuffled list---------#
    numbers = createShuffledList()

    #---------init pygame---------#
    py.init()                                               # init pygame
    width = 1280                                             # set screen width and height
    height = 720
    screen = py.display.set_mode((width, height))           # create screen
    py.display.set_caption("Sorting Algorithm 1")           # set caption from the screen
    running = True

    #-----------main loop------------#
    while running:                                          # main loop checks whether the window is still open
        for event in py.event.get():                        # and will update everything
            if event.type == py.QUIT:
                running = False
        screen.fill((0, 0, 0))                              # background is black

        drawRects(screen, numbers, width, height)           # draw bars


        py.display.update()
        time.sleep(0.1)
    py.quit()

#----------function to draw rects-------------#
def drawRects(screen, lst, width, height):
    bar_width = width // len(lst)                           # every bar has the same width
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

    print(numbersToSort)
    shuffledNumbers = shuffel(numbersToSort)
    print(shuffledNumbers)
    return shuffledNumbers

#----------function to shuffle a list-------------#
def shuffel(lst):
    shuffledNumbers = lst.copy()                        # original list has to be copied in order to shuffle it
    random.shuffle(shuffledNumbers)                     # the copied list is shuffled
    return shuffledNumbers                              # the shuffled list is returned


if __name__ == "__main__":

    n = int(sys.argv[1])
    main(n)

