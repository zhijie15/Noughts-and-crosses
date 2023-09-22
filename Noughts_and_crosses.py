import tkinter as tk
Noughts_and_crosses = tk.Tk()
Noughts_and_crosses.title("Noughts and crosses")
point1 = 0
point2 = 0
turn = 0
def restart():
	global turn
	for i in range(1,10):
		button = eval("B"+str(i))
		button["text"] = ""
		button["state"] = tk.NORMAL
		turn = 0
def check_winner():
	global point1
	global point2
	if B1["text"] == B2["text"] == B3["text"] == "X" or B4["text"] == B5["text"] == B6["text"] == "X" or B7["text"] == B8["text"] == B9["text"] == "X" or B1["text"] == B4["text"] == B7["text"] == "X" or B2["text"] == B5["text"] == B8["text"] == "X" or B3["text"] == B6["text"] == B9["text"] == "X" or B1["text"] == B5["text"] == B9["text"] == "X" or B3["text"] == B5["text"] == B7["text"] == "X":
			point1 = point1 + 1
			result1["text"] = point1
			win["text"] = "Player 1 win"
			restart()
	elif B1["text"] == B2["text"] == B3["text"] == "O" or B4["text"] == B5["text"] == B6["text"] == "O" or B7["text"] == B8["text"] == B9["text"] == "O" or B1["text"] == B4["text"] == B7["text"] == "O" or B2["text"] == B5["text"] == B8["text"] == "O" or B3["text"] == B6["text"] == B9["text"] == "O" or B1["text"] == B5["text"] == B9["text"] == "O" or B3["text"] == B5["text"] == B7["text"] == "O":
			point2 = point2 + 1
			result2["text"] = point2
			win["text"] = "Player 2 win"
			restart()
	elif B1["text"] != "" and  B2["text"] != "" and B3["text"] != "" and B4["text"] != "" and B5["text"] != "" and B6["text"] != "" and B7["text"] != "" and B8["text"] != "" and B9["text"] != "":
			win["text"] = "draw"
			restart()
def B(card):
	global turn
	global who_win 
	global point1
	global point2 
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
	check_winner()
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
win = tk.Label(Noughts_and_crosses, text = "")
win.grid(row = 5, column = 1, padx = 1, pady = 1)
Brestart = tk.Button(Noughts_and_crosses, text="Restart", command = restart) 
Brestart.grid(row=5, column=2)
Noughts_and_crosses.mainloop()
