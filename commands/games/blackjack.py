import random

class Blackjack:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(p, self.deck) for p in players]
    pass

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = Hand(deck.first_hand())
        self.value = self.hand.calculate_value()
    
    def __repr__(self):
        hand = "".join(
            [card.ascii_card() for card in self.hand.cards]
        )
        return f'{self.name}:\n {hand}'

class Hand:
    def __init__(self, cards = []):
        self.cards = cards
        self.blackjack = self.calculate_value() == 21

    def calculate_value(self):
        return sum([card.value for card in self.cards])

    def __repr__(self):
        
        return ''.join([card.ascii_card() for card in self.cards])


class Card:
    def __init__(self, num, suit):
        self.suit = suit
        self.number = num
        self.value = self.calculate_value()
    
    def ascii_card(self):
        spacing = 7
        spacer_line = f"|{' ' * spacing}|\n"
        top_bottom_line = f" {'-' * spacing}\n"
        return f"{top_bottom_line}" \
               f"|{self.suit}{' ' * (spacing-2)}{self.number}|\n" \
                f"{spacer_line * 3}" \
                f"|{self.number}{' ' * (spacing-2)}{self.suit}|\n" \
                f"{top_bottom_line}" \
                f"Value: {self.value}\n"

    def calculate_value(self):
        if self.number == 'J' or self.number == 'Q' or self.number == 'K':
            return 10
        elif self.number == 'A':
            return 11
        else:
            return self.number

class Deck:
    def __init__(self):
        self.remaining_cards = []
        self.init_deck()

    def first_hand(self):
        return [self.remaining_cards.pop(), self.remaining_cards.pop()]


    def init_deck(self):
        graphical_suit = ["S","H","D","C"]
        numbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        deck = [
            Card(number, suit) 
            for number in numbers 
            for suit in graphical_suit
        ]
        random.shuffle(deck)
        self.remaining_cards = deck



if __name__ == '__main__':
    game = Blackjack(['Colby', 'Colby2'])
    for player in game.players:
        print(player, f"Blackjack: {player.hand.blackjack}")