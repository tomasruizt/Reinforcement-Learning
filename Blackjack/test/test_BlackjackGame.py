import unittest
from unittest.mock import MagicMock

from Blackjack.BlackjackGame import BlackjackGame
from Blackjack.Player import Player
from Blackjack.PokerCardsDeck import PokerCardsDeck


class BlackjackGameTest(unittest.TestCase):

    def test_deals_no_more_cards_than_deck_has(self):
        deck = PokerCardsDeck()
        mock_player = MagicMock(spec=Player)
        mock_player.wants_new_card.return_value = True
        players = [mock_player] * 100
        game = BlackjackGame(shuffled_deck=deck, players=players)

        all_player_cards = game.simulate_and_return_player_cards()
        total_number_of_cards = sum(len(cards) for cards in all_player_cards)
        self.assertEqual(total_number_of_cards, 52)
