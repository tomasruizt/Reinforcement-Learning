from Blackjack.Card import Card
from Blackjack.Player import Player
from Blackjack.PokerCardsDeck import PokerCardsDeck
from typing import List


class BlackjackGame:
    """
    In this repeated game a list of players face each other in order following
    the rules of the Blackjack card game.
    """

    def __init__(self, shuffled_deck: PokerCardsDeck, players: List[Player]):
        """
        The Blackjack game starts out with a shuffled deck and will take a list of
        players to play the game. By convention the last player will be the dealer.
        :param shuffled_deck: A newly shuffled deck
        :param players: list of Players
        """
        self._shuffled_deck = shuffled_deck
        self._players = players

    def player_score_under_22(self, player_cards: List[Card]) -> bool:
        """
        This method determines whether the Player's score, based on his Cards, is
        still below 22. In that case, they may still draw, if they want to.
        This method always considers Aces score to be 1.
        :param player_cards: the Card(s) this player has already been dealt.
        :return: A bool value whether Player's score is over 21 or not
        """
        player_score = sum([min(card.value) for card in player_cards])
        return player_score < 22

    # TODO: Document this class
    def simulate_and_return_player_cards(self) -> List[List[Card]]:
        """

        :return:
        """
        all_player_cards = []
        for player in self._players:
            current_player_cards = []
            while self.player_score_under_22(current_player_cards) and player.wants_new_card():
                if not self._shuffled_deck.cards_remaining():
                    all_player_cards.append(current_player_cards)
                    return all_player_cards
                new_card = self._shuffled_deck.draw_card()
                player.accept_card(card=new_card)
                current_player_cards.append(new_card)
            all_player_cards.append(current_player_cards)