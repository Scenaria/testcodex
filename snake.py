import curses
from random import randint

# initialize screen
stdscr = curses.initscr()
# no delay on getch
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
win = curses.newwin(sh, sw, 0, 0)
win.keypad(1)
win.timeout(100)

snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2]
win.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0

try:
    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, 27]:
            key = key

        if key == 27:
            break

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [randint(1, sh-2), randint(1, sw-2)]
                food = nf if nf not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
finally:
    curses.endwin()
