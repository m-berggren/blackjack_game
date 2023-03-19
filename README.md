# Blackjack Game
A simple Blackjack game played through the CLI.

Walkthrough:
- You and the computer get two cards in the beginning, computer only shows one.
- You may decide to take more cards by typing '**hit**' or '**stand**' when you wish to stay.
- Cards 2-9 count at face value, tens and face cards count as 10, and Aces count as 1 or 11.
- You can take cards until you reach 21 points or over.
- When you stop, hit 21 or over, the turn goes to the computer who must draw cards until points reach 16 or more.
- If the computer goes over 21 points you will win regardless of your total points.
- If none of you reach 21 points the winner is the one with most card value. If total points are equal it's a draw.


## To play:
Typically, run this game through CLI:


**Windows:**

```
python blackjack.py
```
**Mac / Linux:**
```
python3 blackjack.py
```
Or, by running blackjack.py through your IDE, e.g. VSCode.


## External libraries
None

## Licence
MIT