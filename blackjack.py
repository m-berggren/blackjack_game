from blackjack_classes import Computer, Deck, User


def main():
    """Main program sets up and evaluates boolean results."""

    print("\nVälkommen till Blackjack\n")
    deck = Deck()
    user = User(deck)
    computer = Computer(deck)

    user = user.play()
    computer = computer.play()

    if user <= 21 and user > computer:
        print("\nGrattis, du vann!\n")

    elif computer <= 21 and computer > user:
        print("Du förlorade.\n")

    elif computer > 21:
        print("Grattis, du vann!\n")

    elif user > 21:
        print("Du förlorade.\n")

    elif user == computer:
        print("Oavgjort.\n")


if __name__ == "__main__":
    main()
