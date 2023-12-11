import tkinter as tk






# m = tkinter.Tk()
# m.mainloop()

# btn = Button






class TicTacToe3D:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("3D Cubic Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]



if __name__ == "__main__":
    TicTacToe3D()