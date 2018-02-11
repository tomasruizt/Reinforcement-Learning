import unittest
from typing import List
from unittest.mock import MagicMock

from Blackjack.BlackjackGame import BlackjackGame
from Blackjack.Player import Player
from Blackjack.PokerCardsDeck import PokerCardsDeck


class BlackjackGameTest(unittest.TestCase):

    def test_deals_no_more_cards_than_deck_has(self):
        players = self.setup_players(num_of_players=100, want_cards=True)
        game = BlackjackGame(shuffled_deck=PokerCardsDeck(), players=players)

        self.assertRaises(Exception, game.play_game)

    def test_play_game_each_player_plays(self):
        players = self.setup_players(4, want_cards=True)
        game = BlackjackGame(shuffled_deck=PokerCardsDeck(), players=players)

        game.play_game()

        for player in players:
            player.wants_new_card.assert_called_with()
            player.accept_card.assert_called()

    def test_play_game_at_least_two_cards_per_player(self):
        players = self.setup_players(num_of_players=8, want_cards=False)
        game = BlackjackGame(shuffled_deck=PokerCardsDeck(), players=players)

        all_player_hands = game.play_game()

        for hand in all_player_hands:
            self.assertTrue(len(hand) >= 2)

    # TODO: Complete tests
    def test_player_score_under_22_21_passes(self):
        pass

    def test_player_score_under_22_22_fails(self):
        pass

    def test_player_score_under_22_aces(self):
        pass

    def setup_players(self, num_of_players: int, want_cards: bool) -> List[Player]:
        players = [MagicMock(spec=Player) for _ in range(num_of_players)]
        for player in players:
            player.wants_new_card.return_value = want_cards
        return players
