from random import shuffle

from Blackjack.Card import Card


class PokerCardsDeck:
    """
    Simulates a shuffled Poker card deck with 52 cards
    """

    def __init__(self):
        """
        Initiates the deck and shuffles the cards.
        """
        self._remaining_cards = [Card(str(i), [i]) for i in range(1, 10)] * 4
        face_cards_values = [
            Card("A", [11, 1]),
            Card("K", [10]),
            Card("Q", [10]),
            Card("J", [10])
        ]
        self._remaining_cards.extend(face_cards_values * 4)
        shuffle(self._remaining_cards)

    def draw_card(self):
        """
        Remove a single Card from the shuffled deck.
        :return: The removed Card. If the deck is empty, this method returns None.
        """
        if len(self._remaining_cards) > 0:
            return self._remaining_cards.pop()
        else:
            return None

    def cards_remaining(self) -> bool:
        return len(self._remaining_cards) > 0
