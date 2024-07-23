import random
import tkinter as tk
ls_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Q', 'Y', 'Z']
ls_2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ls_3 = ['@', '!', '#', '$', '%', '&', '*']
length = int(input("Type the number of characters you want in your password : "))
#lengths = len(length)
num1 = int(input("Type the number of Alphabets you want in your password : "))
#num_1 = len(num1)
num2 = int(input("Type the number of Numbers you want in your password : "))
#num_2 = len(num2)
num3 = int(input("Type the number of Special Characters you want in your password : "))
#num_3 = len(num3)
alphabet = ""
numbers = ""
char = ""
for n in range(0, num1):
    choice_1 = random.choice(ls_1)
    alphabet += choice_1
for n in range(0, num2):
    choice_2 = random.choice(ls_2)
    numbers += choice_2
for n in range(0, num3):
    choice_3 = random.choice(ls_3)
    char += choice_3
password = alphabet + numbers + char
password_shuffled = ''.join(random.sample(password, len(password)))
print(password_shuffled)
root = tk.Tk()
root.geometry("300x75")
labels= tk.Label(root, text="Your password is", font=("Arial", 24))
labels.pack()
label = tk.Label(root, text=password_shuffled, font=("Arial", 14))
label.pack()
root.mainloop()