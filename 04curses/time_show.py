#!/usr/bin/env python
# coding=utf8
#ref http://docs.python.org/2/library/curses.html
#ref http://docs.python.org/2/library/thread.html
from threading import Thread
from time import sleep,time,strftime,localtime
import signal
import sys

from curses.textpad import Textbox
def show_time(win):
    global text
    while True:
        y,x = curses.getsyx()
        win.clear()
        my,mx=scr.getmaxyx()
        win.attrset(curses.color_pair(2))
        win.attrset(curses.color_pair(1))
        win.addstr(0,0,"mx=%d my=%d"%(mx,my))
        win.addstr(1,0,"x=%d y=%d"%(x,y))
        win.addstr(2,0,strftime('%Y-%m-%d %H:%M:%S', localtime(time())))
        win.refresh()
        curses.setsyx(y,x)
        scr.move(y,x)
        scr.refresh()
        sleep(1)
    
def signal_handler(signal, frame):
        sys.exit(0)

import curses
from  curses import panel
if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)

    import locale
    locale.setlocale(locale.LC_ALL, '')
    global scr

    scr = curses.initscr()
    curses.noecho()
    curses.cbreak();scr.keypad(3)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    win =scr.subwin(3,20,6,0)
    global text

    key = ord(' ')
    text=""
    t = Thread(target=show_time, args=(win,))
    t.daemon=True   
    t.start()
    box=Textbox(scr.subwin(1,10,10,0)) 
    win=scr.subwin(3,20,0,0)
    while key != ord('q'):
        curses.napms(10)
        win.addstr(0,0,"Input: %-10s" %(text))
        win.addstr(1,0,"%-10s"%(curses.keyname(key)),curses.A_BOLD)
        win.refresh()
        if key==(curses.KEY_LEFT):
            win.addstr(2,0,"<")
        if key==(curses.KEY_RIGHT):
            win.addstr(2,0,">")
        if key == curses.KEY_UP: 
            win.addstr(2, 0, "^")
        if key == curses.KEY_DOWN: 
            win.addstr(2,0 , "_")
        if curses.keyname(key) == "e": 
            text=box.edit()
        key = scr.getch()
    curses.endwin()
    sys.exit(0)
