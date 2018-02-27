import unittest

from collections import Counter
from numpy import random

from Scenarios.Blackjack.Card import Card
from Scenarios.Blackjack.PokerCardsDeck import PokerCardsDeck


class PokerCardsDeckTest(unittest.TestCase):

    def test_not_every_new_deck_equal(self):
        """
        This test goes through two decks and checks whether both decks have the
        same cards in the same order. In that case, the test fails.
        :return: None
        """
        random.seed(0)

        deck1 = PokerCardsDeck()
        deck2 = PokerCardsDeck()

        equal_order = True
        for _ in range(52):
            equal_order &= equal_order and (
                deck1.draw_card().name == deck2.draw_card().name)

        self.assertFalse(equal_order)

    def test_after_52_cards_returns_None(self):
        deck = PokerCardsDeck()

        for _ in range(52):
            self.assertIsInstance(deck.draw_card(), Card)

        self.assertIsNone(deck.draw_card())

    def test_returns_4_cards_of_each_type(self):
        deck = PokerCardsDeck()
        counter = Counter()

        for _ in range(52):
            card_name = deck.draw_card().name
            counter[card_name] += 1

        card_frequencies = counter.values()
        self.assertEqual(max(card_frequencies), 4)
        self.assertEqual(min(card_frequencies), 4)

    def test_A_has_values_1_and_11(self):
        deck = PokerCardsDeck()

        card = deck.draw_card()
        while card.name is not "A":
            card = deck.draw_card()

        self.assertIn(1, card.value)
        self.assertIn(11, card.value)

    def test_cards_remaining(self):
        deck = PokerCardsDeck()
        for _ in range(51):
            deck.draw_card()

        self.assertTrue(deck.cards_remaining())
        deck.draw_card()
        self.assertFalse(deck.cards_remaining())
