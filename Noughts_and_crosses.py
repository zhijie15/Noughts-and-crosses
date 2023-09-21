import tkinter as tk
Noughts_and_crosses = tk.Tk()
Noughts_and_crosses.title("Noughts and crosses")
point1 = 0
point2 = 0
turn = 0
who_win = ""
def B(card):
	global turn
	global who_win 
	global point1
	if turn == 0:
		button = eval("B" + str(card))
		button ["text"] = "X"
		button["state"] = tk.DISABLED
		turn = 1
	else:
		button = eval("B" + str(card))
		button ["text"] = "O"
		button["state"] = tk.DISABLED
		turn = 0 
	 
		
Player_1 = tk.Label(Noughts_and_crosses, text = "Player 1:")
Player_1.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
Player_2 = tk.Label(Noughts_and_crosses, text = "Player 2:")
Player_2.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 1)
result1 = tk.Label(Noughts_and_crosses, text = point1)
result1.grid(row = 0, column = 2, padx = 1, pady = 1)
result2 = tk.Label(Noughts_and_crosses, text = point2)
result2.grid(row = 1, column = 2, padx = 1, pady = 1)
B1 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(1))
B1.grid(row = 2, column = 0,  padx = 1, pady = 1)
B2 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(2))
B2.grid(row = 2, column = 1,  padx = 1, pady = 1)
B3 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(3))
B3.grid(row = 2, column = 2,  padx = 1, pady = 1)
B4 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(4))
B4.grid(row = 3, column = 0,  padx = 1, pady = 1)
B5 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(5))
B5.grid(row = 3, column = 1,  padx = 1, pady = 1)
B6 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(6))
B6.grid(row = 3, column = 2,  padx = 1, pady = 1)
B7 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(7))
B7.grid(row = 4, column = 0,  padx = 1, pady = 1)
B8 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(8))
B8.grid(row = 4, column = 1,  padx = 1, pady = 1)
B9 = tk.Button(Noughts_and_crosses, text = "",width = 10, height = 4, command = lambda:B(9))
B9.grid(row = 4, column = 2,  padx = 1, pady = 1)
win = tk.Label(Noughts_and_crosses, text = who_win)
win.grid(row = 5, column = 1, padx = 1, pady = 1)
Noughts_and_crosses.mainloop()
