import tkinter as tk
from tkinter import ttk
import random

def spin_slot():
    slot_list = ["💰", "💎", "👑", "⭐"]
    return [random.choice(slot_list) for _ in range(3)]

def calc_res(icons, bid):
    if icons[0] == icons[1] == icons[2]:
        match icons[0]:
            case '💰':
                return bid * 2
            case '💎':
                return bid * 5
            case '👑':
                return bid * 10
            case '⭐':
                return bid * 100
    return 0

def spin():
    try:
        bid_amount = int(bid.get())
    except ValueError:
        result_label.config(text="❌ Invalid input. Enter a number.", foreground="red")
        return

    if bid_amount <= 0:
        result_label.config(text="❌ Enter amount greater than 0.", foreground="red")
        return
    elif bid_amount > balance.get():
        result_label.config(text="❌ Insufficient balance.", foreground="red")
        return

    # Deduct bid
    balance.set(balance.get() - bid_amount)

    # Spin
    slots = spin_slot()
    slot_display.config(text=" | ".join(slots))

    # Calculate result
    payout = calc_res(slots, bid_amount)
    if payout > 0:
        balance.set(balance.get() + payout)
        result_label.config(text=f"🎉 You won ${payout}!", foreground="green")
    else:
        result_label.config(text="😢 Better luck next time.", foreground="white")

    balance_label.config(text=f"Current Balance: ${balance.get()}")

def close_window():
    window.destroy()

def new_game():
    balance.set(100)
    balance_label.config(text=f"Current Balance: ${balance.get()}")

window = tk.Tk()
window.title("🕹️ Slot Machine")
window.geometry("700x500")
window.config(background="black")

title_font = ('Arial', 20, 'bold')
heading_font = ('Arial', 15, 'bold')
subheading_font = ('Arial', 12, 'bold')

ttk.Label(window, text="Welcome to the Slot Machine 💰 💎 👑 ⭐", background="black", foreground="white", font=title_font).pack(pady=10)
ttk.Label(window, text="💰 - 2x | 💎 - 5x | 👑 - 10x | ⭐ - 100x", background="black", foreground="white", font=subheading_font).pack()

balance = tk.IntVar(value=100)
balance_label = ttk.Label(window, text=f"Current Balance: ${balance.get()}", background="black", foreground="white", font=subheading_font)
balance_label.pack(pady=10)


ttk.Label(window, text="Enter Bid Amount ($):", background="black", foreground="white", font=subheading_font).pack()
bid = tk.StringVar()
ttk.Entry(window, textvariable=bid).pack(pady=5)

spin_btn = ttk.Button(window, text="🎰 Spin", command=spin).pack(pady=10)
new_game_btn = ttk.Button(window, text="🔄 Restart", command=new_game).pack(pady=10)
exit_btn  = ttk.Button(window, text="🚪🚶Exit ", command=close_window).pack(pady=10)

slot_display = ttk.Label(window, text="---|---|--- ", background="black", foreground="white", font=title_font)
slot_display.pack(pady=20)

result_label = ttk.Label(window, text="", background="black", foreground="white", font=subheading_font)
result_label.pack(pady=10)



window.mainloop()
