import random

def get_card_name(card):
    if card == 11:
        return "Ace"
    elif card == 12:
        return "Jack"
    elif card == 13:
        return "Queen"
    elif card == 14:
        return "King"
    else:
        return str(card)

def pic_card():
    card1 = random.randint(1, 14)
    card2 = random.randint(1, 14)

    # Ensure the initial cards are not over 21
    while card1 + card2 > 21 or card1 + card2 == 21:
        card2 = random.randint(1, 14)

    total = card1 + card2
    print(f"Card 1: {get_card_name(card1)}, Card 2: {get_card_name(card2)}\nTotal: {total}")
    return total

def calc(total, dep, bet):
    balance = dep  # Initialize balance before entering the loop

    while total < 21:
        decision = input("Choose whether you want to hit or stand: ")

        if decision.lower() == "hit":
            card = random.randint(1, 14)
            card_name = get_card_name(card)
            print(f"Card: {card_name}")
            total += card
            print(f"Total: {total}")

            if total > 21:
                print(f"BUSTED! You got {total} and lost the game.")
                balance -= bet
                print(f"Balance left: {balance}")
                break
            elif total == 21:
                print(f"LESSGO! You got {total} and won the game!")
                balance += 2 * bet
                print(f"Balance left: {balance}")
                break

        elif decision.lower() == "stand":
            dealer1 = random.randint(1, 14)
            dealer2 = random.randint(1, 14)
            deal_tot = dealer1 + dealer2

            print(f"Dealer's Card 1: {get_card_name(dealer1)}, Card 2: {get_card_name(dealer2)}")
            print(f"Dealer's total: {deal_tot}")

            if deal_tot > total and deal_tot<=21:
                print("Dealer wins! You lose.")
                balance -= bet
                print(f"Balance left: {balance}")
            elif deal_tot > 21:
                print("You win! Dealer loses.")
                balance += 2 * bet
                print(f"Balance left: {balance}")
            elif deal_tot < total:
                print("You win! Dealer loses.")
                balance += 2 * bet
                print(f"Balance left: {balance}")
            else:
                print("It's a tie!")

            break

    return balance  # Return the updated balance after each round

def blackjack_game(dep):
    bet = float(input("Place your bet: "))

    if dep <= 0:
        print("Invalid deposit amount. Exiting the game.")
        return

    initial_total = pic_card()
    remaining_balance = calc(initial_total, dep, bet)

    return remaining_balance  # Return the remaining balance after each round

if __name__ == "__main__":
    initial_deposit = float(input("How much do you want to deposit ($): "))

    while initial_deposit > 0:
        initial_deposit = blackjack_game(initial_deposit)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing! Goodbye.")
            break
    else:
        print("Invalid deposit amount. Exiting the game.")
