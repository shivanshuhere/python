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



def main():
    print("Welcome to slot game 💰 💎 👑 ⭐ \n")
    print(f"Rules".center(20,"-"))
    print("💰 - 2x Amount \n💎 - 5x Amount \n👑 - 10x Amount \n⭐ - 100x Amount\n")
    balance = 100
    while balance > 0:
        print(f"Current Balance - ${balance}\n")
        bid = input("Bid amount - $")
        if not bid.isdigit() :
            print("Invalid amount")
            continue

        bid = int(bid)
        if bid <= 0 :
            print("Enter amount greater than 0$\n")
            continue
        elif bid > balance :
            print(f"Insufficient Balance \n")
            continue
    
        balance -= bid
        
        row = spin_slot()
        print_slot(row)
        payout = calc_res(row, bid)
        
        if payout > bid:
            balance += payout
            print(f"🎉 Congratulations!..You win ${payout}\n")
        else:
            print("Better luck next time..\n")
            
        choice = input("Do you want to spin again? (Y/N): ").upper()        
        if choice != 'Y':
            break
    print("----------------------------------------------")
    print(f"Game Over! Your final balance - ${balance}")
    print("----------------------------------------------")
    
            
if __name__ == "__main__":
    main()