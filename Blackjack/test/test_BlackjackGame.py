import unittest
from typing import List
from unittest.mock import MagicMock

from Blackjack.BlackjackGame import BlackjackGame
from Blackjack.Card import Card
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

    def test_player_score_under_22_21_passes(self):
        player = MagicMock(spec=Player)
        player.wants_new_card.side_effect = [True, False] # Gets to 21 and stays

        game = BlackjackGame(shuffled_deck=self.setup_deck(), players=[player])
        all_player_hands = game.play_game()

        self.assertTrue(len(all_player_hands) is 1)
        self.assertTrue(len(all_player_hands[0]) is 3)

    def test_player_score_under_22_22_fails(self):
        player = MagicMock(spec=Player)
        player.wants_new_card.side_effect = [True, True] # Draws too many and gets 22

        game = BlackjackGame(shuffled_deck=self.setup_deck(), players=[player])
        all_player_hands = game.play_game()

        self.assertTrue(len(all_player_hands) is 1)
        self.assertTrue(len(all_player_hands[0]) is 4)

    def test_player_score_under_22_aces(self):
        player = MagicMock(spec=Player)
        player.wants_new_card.side_effect = [True, True, True, False]
        # gathers 4 aces and is still able to draw

        game = BlackjackGame(shuffled_deck=self.setup_deck_aces(), players=[player])
        all_player_hands = game.play_game()

        self.assertTrue(len(all_player_hands) is 1)
        self.assertTrue(len(all_player_hands[0]) is 5)

    def setup_players(self, num_of_players: int, want_cards: bool) -> List[Player]:
        players = [MagicMock(spec=Player) for _ in range(num_of_players)]
        for player in players:
            player.wants_new_card.return_value = want_cards
        return players

    def setup_deck(self):
        cards = [
            Card("10", [10]),
            Card("9", [9]),
            Card("2", [2]),
            Card("A", [11, 1]),
            Card("3", [3])
        ]
        deck = MagicMock(spec=PokerCardsDeck)
        deck.cards_remaining.return_value = True
        deck.draw_card.side_effect = cards
        return deck

    def setup_deck_aces(self):
        cards = [
            Card("A", [1, 11]),
            Card("A", [1, 11]),
            Card("A", [1, 11]),
            Card("A", [1, 11]),
            Card("2", [2])
        ]
        deck = MagicMock(spec=PokerCardsDeck)
        deck.cards_remaining.return_value = True
        deck.draw_card.side_effect = cards
        return deck