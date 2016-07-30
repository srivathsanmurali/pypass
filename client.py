from curses import wrapper
import curses
import database
import config

def initColors():
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

def checkPassword(stdscr):
    initColors()

    #clear screen
    stdscr.clear()

    stdscr.addstr(0,0,"PyPass - A python based password manager\n", curses.color_pair(1))
    stdscr.addstr(1,0,"Database path = {}\n".format(config.pyPassDir), curses.COLOR_WHITE)
    stdscr.addstr(2,0,"Enter master password = \n", curses.COLOR_WHITE)

    stdscr.refresh()
    stdscr.getkey()

def main():
    wrapper(checkPassword)

if __name__ == "__main__":
    main()
