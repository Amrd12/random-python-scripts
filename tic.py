import tkinter as tk
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tic tie toc")
        self.geometry("345x549")
        self.config(bg="white")
        self.resizable(width=False,height=False)
        self.mode = tk.StringVar(value="")  # Store game mode

        # Main frame
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Mode selection buttons
        self.btn_1v1 = tk.Button(self.main_frame, text="1 vs 1", font=("Helvetica", 14), command=lambda: self.make_mode("two"))
        self.btn_1v1.grid(row=0, column=0, padx=10, pady=10)

        self.btn_1vComp = tk.Button(self.main_frame, text="1 vs computer", font=("Helvetica", 14), command=lambda: self.make_mode("one"))
        self.btn_1vComp.grid(row=0, column=1, padx=10, pady=10)

        # Game variables
        self.player1 = ""
        self.player2 = ""
        self.active = "player1"
        self.gameover = False
        self.p1wins = 0
        self.p2wins = 0

        self.create_score_frame()

    def create_score_frame(self):
        self.score_frame = tk.Frame(self.main_frame, bg="white")
        self.score_frame.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(self.score_frame, text="Score: 0 : 0", font=("Helvetica", 16), bg="white")
        self.result_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.player_label = tk.Label(self.score_frame, text="Player 1 turn", font=("Helvetica", 16), bg="white")
        self.player_label.grid(row=1, column=0, columnspan=2, pady=5)

        # Button for another game
        self.another_game_btn = tk.Button(self.score_frame, text="Play Another Game", font=("Helvetica", 14), command=self.play_another_game)
        self.another_game_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def create_board(self, frame):
        self.game_frame = tk.Frame(frame, bg="white")
        self.game_frame.grid(row=2, column=0, columnspan=2)

        # Buttons for game board
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                btn = tk.Button(self.game_frame, text="", font=("Helvetica", 24, "bold"), width=5, height=2,
                                command=lambda x=i, y=j: self.click(x, y))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # Reset button
        self.reset_btn = tk.Button(frame, text="Reset", font=("Helvetica", 18, "bold"), command=self.reset_game)
        self.reset_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def make_mode(self, mode):
        self.mode.set(mode)
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        if mode == 'one':
            self.player1 = "Player 1"
            self.player2 = "Computer"
            self.create_game_frame()
        else:
            self.player1 = "Player 1"
            self.player2 = "Player 2"
            self.create_game_frame()

    def create_game_frame(self):
        self.create_score_frame()
        self.create_board(self.main_frame)

    def click(self, row, col):
        if not self.gameover:
            button = self.buttons[row][col]
            if button["text"] == "":
                button.config(text="X" if self.active == "player1" else "O")
                self.check()
                if not self.gameover:
                    self.active = "player2" if self.active == "player1" else "player1"
                    self.player_label.config(text=f"{self.player2 if self.active == 'player2' else self.player1} turn")
                    if self.mode.get() == "one" and self.active == "player2":
                        self.computer_click()

    def computer_click(self):
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]
        if empty_buttons:
            row, col = random.choice(empty_buttons)
            self.click(row, col)

    def check(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.end_game(self.buttons[i][0]["text"])
                return
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.end_game(self.buttons[0][i]["text"])
                return
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.end_game(self.buttons[0][0]["text"])
            return
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.end_game(self.buttons[0][2]["text"])
            return
        if all(self.buttons[i][j]["text"] for i in range(3) for j in range(3)):
            self.end_game("Draw")
            return

    def end_game(self, winner):
        if winner != "Draw":
            winner = self.player1 if winner == "X" else self.player2
            if winner == self.player1:
                self.p1wins += 1
            else:
                self.p2wins += 1
            self.result_label.config(text=f"Score: {self.p1wins} : {self.p2wins}")
            self.player_label.config(text=f"{winner} wins!")
        else:
            self.player_label.config(text="It's a draw!")
        self.gameover = True
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.active = "player1"
        self.player_label.config(text=f"{self.player1} turn")
        self.gameover = False
        
    def reset_game(self):
        self.p1wins=0
        self.p2wins=0
        self.result_label.config(text="Score: 0 : 0")
        self.reset()

    def play_another_game(self):
        self.reset()


if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
