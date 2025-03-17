import random
from enum import Enum, auto

# Constants
BLACKJACK = 21
DEALER_THRESHOLD = 17
STARTING_BALANCE = 100

class GameStatus(Enum):
    PLAYING = auto()
    BUST = auto()
    BLACKJACK = auto()

class BlackJackGame:
    def __init__(self):
        self.balance = STARTING_BALANCE
        self.bet = 0
        self.deck = self.create_deck()
        self.dealer_cards = []
        self.player_cards = []

    def create_deck(self):
        """Create a shuffled deck of 52 cards with (name, value) tuples."""
        ranks = [
            ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9),
            ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
        ]
        deck = [card for _ in range(4) for card in ranks]
        random.shuffle(deck)
        return deck

    def draw_card(self):
        """Draw a card from the deck, reshuffling if empty."""
        if not self.deck:
            self.deck = self.create_deck()
        return self.deck.pop()

    def calculate_sum(self, cards):
        """Calculate the hand's value, adjusting for Aces."""
        total = sum(card[1] for card in cards)
        aces = sum(1 for card in cards if card[1] == 11)
        while total > BLACKJACK and aces > 0:
            total -= 10
            aces -= 1
        return total

    def display_cards(self, role, cards, hide_first=False):
        """Display the cards, showing names and total if not hidden."""
        if hide_first:
            visible = ['Hidden'] + [card[0] for card in cards[1:]]
            print(f"{role} cards: {visible}")
        else:
            card_names = [card[0] for card in cards]
            total = self.calculate_sum(cards)
            print(f"{role} cards: {card_names} (Total: {total})")

    def place_bet(self):
        """Prompt the player to place a valid bet."""
        while True:
            try:
                bet = int(input(f"Balance: ${self.balance}. Enter bet: $"))
                if 1 <= bet <= self.balance:
                    self.bet = bet
                    return
                print(f"Bet must be between $1 and ${self.balance}.")
            except ValueError:
                print("Please enter a valid number.")

    def player_turn(self):
        """Handle the player's turn, returning True if bust."""
        while True:
            self.display_cards("Player", self.player_cards)
            total = self.calculate_sum(self.player_cards)

            if total > BLACKJACK:
                print("Player busts!")
                return GameStatus.BUST
            elif total == BLACKJACK:
                print("Player has 21!")
                return GameStatus.BLACKJACK

            choice = input("Hit? (y/n): ").strip().lower()
            if choice == 'y':
                self.player_cards.append(self.draw_card())
            elif choice == 'n':
                return GameStatus.PLAYING
            else:
                print("Invalid input. Enter 'y' or 'n'.")

    def dealer_turn(self):
        """Handle the dealer's turn, returning True if bust."""
        self.display_cards("Dealer", self.dealer_cards)
        while self.calculate_sum(self.dealer_cards) < DEALER_THRESHOLD:
            self.dealer_cards.append(self.draw_card())
            self.display_cards("Dealer", self.dealer_cards)

        if self.calculate_sum(self.dealer_cards) > BLACKJACK:
            print("Dealer busts!")
            return True
        return False

    def determine_winner(self):
        """Compare hands and update balance based on outcome."""
        player_sum = self.calculate_sum(self.player_cards)
        dealer_sum = self.calculate_sum(self.dealer_cards)

        if player_sum > dealer_sum:
            print(f"Player wins! +${self.bet}")
            self.balance += self.bet
        elif dealer_sum > player_sum:
            print(f"Dealer wins! -${self.bet}")
            self.balance -= self.bet
        else:
            print("Push. Bet returned.")

    def play(self):
        print("Welcome to Blackjack!")
        while self.balance > 0:
            self.place_bet()
            self.deck = self.create_deck()
            self.player_cards = [self.draw_card(), self.draw_card()]
            self.dealer_cards = [self.draw_card(), self.draw_card()]

            # Check for naturals
            player_natural = len(self.player_cards) == 2 and self.calculate_sum(self.player_cards) == BLACKJACK
            dealer_natural = len(self.dealer_cards) == 2 and self.calculate_sum(self.dealer_cards) == BLACKJACK

            if player_natural:
                self.display_cards("Dealer", self.dealer_cards)
                if dealer_natural:
                    print("Both have Blackjack! Push.")
                else:
                    payout = int(self.bet * 1.5)
                    print(f"Natural Blackjack! You win ${payout}!")
                    self.balance += payout
                continue

            self.display_cards("Dealer", self.dealer_cards, hide_first=True)

            # Player's turn
            player_result = self.player_turn()
            if player_result == GameStatus.BUST:
                self.balance -= self.bet
            else:
                # Dealer's turn
                dealer_bust = self.dealer_turn()
                if dealer_bust:
                    self.balance += self.bet
                else:
                    self.determine_winner()

            print(f"Balance: ${self.balance}")
            if self.balance <= 0:
                print("You're out of funds! Game over.")
                break

            if input("Play again? (y/n): ").lower() != 'y':
                break

        print("Thanks for playing!")

if __name__ == "__main__":
    game = BlackJackGame()
    game.play()
