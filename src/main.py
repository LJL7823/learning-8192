"""
8192 game
"""
import logic
import tkinter as tk
import os


def main():
    mat = logic.start_game()
    print("\t", mat[0], '\n\t', mat[1], '\n\t', mat[2], '\n\t', mat[3], '\n\t')
    while not logic.has_lost(mat):
        new_mat = []
        x = input("Press the command : ")
        if x == 'W' or x == 'w':
            new_mat = logic.move_up(mat)
            status = logic.has_lost(new_mat)
            print(status)
            if not status:
                logic.add_two(new_mat)
            else:
                break
        elif x == 'S' or x == 's':
            new_mat = logic.move_down(mat)
            status = logic.has_lost(new_mat)
            print(status)
            if not status:
                logic.add_two(new_mat)
            else:
                break

        # to move left
        elif x == 'A' or x == 'a':
            new_mat = logic.move_left(mat)
            status = logic.has_lost(new_mat)
            print(status)
            if not status:
                logic.add_two(new_mat)
            else:
                break

        # to move right
        elif x == 'D' or x == 'd':
            new_mat = logic.move_right(mat)
            status = logic.has_lost(new_mat)
            print(status)
            if not status:
                logic.add_two(new_mat)
            else:
                break
        elif x == "QT" or x == "qt":
            exit(0)
        else:
            print("Invalid Key Pressed")

        # print the matrix after each
        # move.
        mat = new_mat
        print("\t", new_mat[0], '\n\t', new_mat[1], '\n\t', new_mat[2], '\n\t',
              new_mat[3])


if __name__ == '__main__':
    game_screen = tk.Tk()
    frm = tk.Frame(game_screen)
    frm.grid()
    tk.Label(frm, text="Hello World!").grid(column=0, row=0)
    tk.Button(frm, text="Quit", command=game_screen.destroy).grid(column=1,
                                                                  row=0)
    game_screen.mainloop()
    main()
