import tkinter as tk
from tkinter import ttk
import random

def spin_slot():
    slot_list = ["💰", "💎", "👑", "⭐"]
    return [ random.choice(slot_list) for _ in range(3)]

def print_slot(row):
    print("---------------")
    print(f" | ".join(row))
    print("---------------")

def calc_res(icons, bid):
    if icons[0] == icons[1] == icons[2]:
        match icons[0] :
            case '💰':
                return bid*2
            case '💎':
                return bid*5
            case '👑':
                return bid*10
            case '⭐':
                return bid*100
    else:
        return 0




window = tk.Tk()
window.title("🕹️ Slot Machine")
window.geometry("700x600")
window.config(background="black")

title_font = ('Arial', 20, 'bold')
heading_font = ('Arial', 15, 'bold')
subheading_font = ('Arial', 12, 'bold')
ttk.Label(text="Welcome to slot machine 💰 💎 👑 ⭐ ", background="black", foreground="white", font=title_font).pack(pady=20, padx=20)
ttk.Label(text=f"Rules", background="black", foreground="white", font=heading_font).pack( padx=20)
ttk.Label(text="💰 - 2x Amount \n💎 - 5x Amount \n👑 - 10x Amount \n⭐ - 100x Amount\n", background="black", foreground="white", font=subheading_font).pack()
balance = tk.IntVar(value=100)
while balance.get() > 0:
        ttk.Label(text=f"Current Balance - ${balance.get()}", background="black", foreground="white", font=subheading_font).pack()
        
        # bid = input("Bid amount - $")
        ttk.Label(text="Bid amount - $", background="black", foreground="white", font=subheading_font).pack()
        bid = tk.StringVar()
        # ttk.Entry(window, textvariable=bid).pack(pady=10)
        if not bid.get().isdigit() :
            ttk.Label(text="Invalid amount", background="black", foreground="white", font=subheading_font).pack()
            continue

        bid.get(int(bid.get()))
        if bid.get() <= 0 :
            ttk.Label(text="Enter amount greater than 0$", background="black", foreground="white", font=subheading_font).pack()
            continue
        elif bid.get() > balance.get() :
            ttk.Label(text="Insufficient Balance ", background="black", foreground="white", font=subheading_font).pack()
            continue
    
        balance.set(balance.get() - bid.get())
        row = tk.list()
        row = spin_slot()
        print_slot(row)
        payout  = tk.IntVar()
        payout.set(calc_res(row, bid.get()))
        
        if payout.get() > bid.get():
            balance.set(balance.get() + payout.get())
            ttk.Label(text=f"🎉 Congratulations!..You win ${payout}", background="black", foreground="white", font=subheading_font).pack()
        else:
            # print("Better luck next time..\n")
            ttk.Label(text=f"Better luck next time", background="black", foreground="white", font=subheading_font).pack()
            
        # choice = input("Do you want to spin again? (Y/N): ").upper()  
        #     ttk.Label(text=f"🎉 Congratulations!..You win ${payout}", background="black", foreground="white", font=subheading_font).pack()
        # if choice != 'Y':
        #     break
    # print("----------------------------------------------")
    # print(f"Game Over! Your final balance - ${balance}")
    # print("----------------------------------------------")

window.mainloop()