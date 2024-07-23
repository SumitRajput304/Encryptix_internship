import random
import tkinter as tk
choice = random.randint(1,3)
def stop(should):
    if should == "yes":
        should_continue = False
    else:
        should_continue = True
def logic(number):
    input = number
    if input == "1":
        if choice == 1:
            print("Tie")
        elif choice == 2:
            print("You Lose")
        elif choice == 3:
            print("You Win")
    elif input == "2":
        if choice == 1:
            print("You Win")
        elif choice == 2:
            print("Tie")
        elif choice == 3:
            print("You Lose")
    elif input == "3":
        if choice == 1:
            print("You Lose")
        elif choice == 2:
            print("You Win")
        elif choice == 3:
            print("Tie")
    else:
        print("Invalid input")
root = tk.Tk()
root.geometry("150x75")
btn_rock = tk.Button(root, text="Rock", command=lambda:logic("1"), width= 5)
btn_rock.grid(row=1, column=1)
btn_paper = tk.Button(root, text="Paper", command=lambda:logic("2"), width= 5)
btn_paper.grid(row=1, column=2)
btn_scissor = tk.Button(root, text="Scissor", command=lambda:logic("3"), width= 5)
btn_scissor.grid(row=1, column=3)
btn_quit = tk.Button(root, text="Quit", command=lambda:stop("Yes"), width= 5)
btn_quit.grid(row=2, column=1)
btn_play = tk.Button(root, text="Play", command=lambda:stop("No"), width= 5)
btn_play.grid(row=2, column=3)
root.mainloop()
