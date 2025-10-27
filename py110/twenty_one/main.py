"""
This module implements the game logic for Twenty-One (Blackjack).
It handles deck creation, card dealing, player and dealer turns, score
calculation, and win conditions.
"""

import random

DECK = [
    ["hearts", "2", 2],
    ["hearts", "3", 3],
    ["hearts", "4", 4],
    ["hearts", "5", 5],
    ["hearts", "6", 6],
    ["hearts", "7", 7],
    ["hearts", "8", 8],
    ["hearts", "9", 9],
    ["hearts", "10", 10],
    ["hearts", "Jack", 10],
    ["hearts", "Queen", 10],
    ["hearts", "King", 10],
    ["hearts", "Ace", 11],
    ["diamonds", "2", 2],
    ["diamonds", "3", 3],
    ["diamonds", "4", 4],
    ["diamonds", "5", 5],
    ["diamonds", "6", 6],
    ["diamonds", "7", 7],
    ["diamonds", "8", 8],
    ["diamonds", "9", 9],
    ["diamonds", "10", 10],
    ["diamonds", "Jack", 10],
    ["diamonds", "Queen", 10],
    ["diamonds", "King", 10],
    ["diamonds", "Ace", 11],
    ["clubs", "2", 2],
    ["clubs", "3", 3],
    ["clubs", "4", 4],
    ["clubs", "5", 5],
    ["clubs", "6", 6],
    ["clubs", "7", 7],
    ["clubs", "8", 8],
    ["clubs", "9", 9],
    ["clubs", "10", 10],
    ["clubs", "Jack", 10],
    ["clubs", "Queen", 10],
    ["clubs", "King", 10],
    ["clubs", "Ace", 11],
    ["spades", "2", 2],
    ["spades", "3", 3],
    ["spades", "4", 4],
    ["spades", "5", 5],
    ["spades", "6", 6],
    ["spades", "7", 7],
    ["spades", "8", 8],
    ["spades", "9", 9],
    ["spades", "10", 10],
    ["spades", "Jack", 10],
    ["spades", "Queen", 10],
    ["spades", "King", 10],
    ["spades", "Ace", 11]
]

player = []
dealer = []

def prompt(message):
    """
    Prints a formatted message to the user.
    Parameters:
        message (str): The message to be displayed.
    Returns:
        None
    """
    print(f"=> {message}")


def deal_card(deck):
    """
        Deals a new card to the player and removes it from the deck
        Parameters:
            deck (list)
        Returns:
            new card
        """
    new_card = random.choice(deck)
    deck.remove(new_card)
    return new_card


def deal_initial_hand(deck):
    """
        deals the initial hand for both players.

        Parameters:
            deck (list): the card deck used in the game

        Returns:
            The initial hand for each user
        """
    global player
    global dealer

    player = [deal_card(deck), deal_card(deck)]
    dealer = [deal_card(deck), deal_card(deck)]

    return f"""
    Dealer has: a {dealer[0][1]} of {dealer[0][0]} and an unknown card\nYou
    have: {player[0][1]} of {player[0][0]} and {player[1][1]} of {player[1][0]}
    """


def calculate_total(hand):
    """
        Calculates the total points in the players' hand

        Parameters:
            player's hand (list)

        Returns:
            total points (int)
        """
    ranks = [card[1] for card in hand]
    total = 0
    for rank in ranks:
        if rank == "Ace":
            total += 11
        elif rank in ["Jack", "Queen", "King"]:
            total += 10
        else:
            total += int(rank)

    aces = ranks.count("Ace")
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def busted(hand):
    """
        Determines if the given hand is bust (total > 21).
        Parameters:
            hand (list): List of cards representing a hand.
        Returns:
            bool: True if the hand's total value exceeds 21, False otherwise.
        """
    return calculate_total(hand) > 21


def dealer_turn(deck):
    """
        Play logic for the dealer
        Parameters:
            deck (list): List of cards still in the game.
        Returns:
            None
        """
    while calculate_total(dealer) < 17:
        dealer.append(deal_card(deck))


def player_turn(deck):
    """
            Play logic for the dealer
            Parameters:
                deck (list): List of cards still in the game.
            Returns:
                None
            """
    while True:
        answer = input('Would you like to hit or stay?').lower()
        if answer == "stay":
            prompt("You chose to stay. Dealer's turn")
            dealer_turn(deck)
            return

        player.append(deal_card(deck))
        if calculate_total(player) > 21:
            prompt('You busted!')
            break

        for card in player:
            print(f"You have: {card[1]} of {card[0]}")


def format_hand(hand):
    """
    formats the information on player's hands.
    Parameters:
        hand (list): List of cards for each player.
    Returns:
        A formatted string
            """
    return ', '.join(f"{rank} of {suit}" for suit, rank, _ in hand)

def determine_winner(player_hand, dealer_hand):
    """
        Determines the winner
        Parameters:
            player_hand, dealer_hand (list): List of cards for each player.
        Returns:
            the result (String)
                """
    pt = calculate_total(player_hand)
    dt = calculate_total(dealer_hand)

    if pt > 21:
        return 'player_bust'
    if dt > 21:
        return 'dealer_bust'
    if pt > dt:
        return 'player'
    if dt > pt:
        return 'dealer'
    return 'tie'  # push


def display_result(player_hand, dealer_hand):
    """
        Displays the result
        Parameters:
            player_hand, dealer_hand (list): List of cards for each player.
        Returns:
            None
                """
    result = determine_winner(player_hand, dealer_hand)
    pt = calculate_total(player_hand)
    dt = calculate_total(dealer_hand)

    print(f"Dealer has: {format_hand(dealer_hand)} (total: {dt})")
    print(f"You have: {format_hand(player_hand)} (total: {pt})")

    if result == 'player_bust':
        prompt("You busted. Dealer wins.")
    elif result == 'dealer_bust':
        prompt("Dealer busted. You win!")
    elif result == 'player':
        prompt("You win!")
    elif result == 'dealer':
        prompt("Dealer wins.")
    else:
        prompt("It's a tie!")


prompt("Welcome to TWENTY-ONE")
print(deal_initial_hand(DECK))

player_turn(DECK)  # this already runs dealer_turn if player stays

# Show final outcome
display_result(player, dealer)
