#!/usr/bin/env python
# coding=utf8
#ref http://docs.python.org/2/library/curses.html
import curses
if __name__=="__main__":
    import locale
    locale.setlocale(locale.LC_ALL, '')

    scr = curses.initscr()
    curses.noecho()
    curses.cbreak();scr.keypad(1)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    scr.clear()

    scr.attrset(curses.color_pair(2))
    scr.addstr(0,0,"Input key:")
    scr.addstr(1,0,"")
    scr.attrset(curses.color_pair(1))

    key = ''
    while key != ord('q'):
        curses.napms(100)
        key = scr.getch()
        if key==(curses.KEY_LEFT):
            scr.addstr(2,0,"<")
        if key==(curses.KEY_RIGHT):
            scr.addstr(2,0,">")
        if key == curses.KEY_UP: 
            scr.addstr(2, 0, "^")
        elif key == curses.KEY_DOWN: 
            scr.addstr(2,0 , "_")
        scr.addstr(1,0,str(key),curses.A_BOLD)
        scr.refresh()
    curses.endwin()
