import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol configurations
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def deposit():
    while True:
        try:
            amount = int(input("What would you like to deposit? $"))
            if amount > 0:
                return amount
            else:
                print("Amount must be more than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_num_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Lines must be between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def get_bet():
    while True:
        try:
            amount = int(input(f"What would you like to bet on each line? (${MIN_BET}-{MAX_BET}): $"))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")

def get_slot_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_win(columns, lines, bet, values):
    winnings = 0
    win_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            win_lines.append(line + 1)

    return winnings, win_lines

def game(balance):
    lines = get_num_of_lines()
    bet = get_bet()

    total_bet = bet * lines
    if total_bet > balance:
        print(f"You don't have enough money to bet ${total_bet}. Your current balance is ${balance}.")
        return 0

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    # Simulate slot spin
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)

    winnings, win_line = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    if win_line:
        print(f"You won on line(s): {', '.join(map(str, win_line))}")

    return winnings - total_bet

def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit): ")
        if spin == "q":
            break
        balance += game(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
