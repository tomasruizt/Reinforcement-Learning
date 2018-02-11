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

    def play_game(self) -> List[List[Card]]:
        """
        Plays a round of of blackjack with the list of Players that were passed
        in the constructor, in the list's order. For each player while wants_new_card()
        returns true and they have not lost, the game will give them a new card.
        :return: A list with the hands of each player, in the order they were passed
        in the constructor.
        """
        all_player_hands = []
        for player in self._players:
            current_player_hand = self.take_turn(player)
            all_player_hands.append(current_player_hand)
        return all_player_hands

    def take_turn(self, player: Player) -> List:
        current_player_hand = []
        for _ in range(2): self.give_new_card(player, current_player_hand)
        while self.player_score_under_22(current_player_hand) and player.wants_new_card():
            self.give_new_card(player, current_player_hand)
        return current_player_hand

    def give_new_card(self, player: Player, hand: List[Card]):
        if not self._shuffled_deck.cards_remaining():
            raise Exception("No more cards remain for player to keep drawing.")
        new_card = self._shuffled_deck.draw_card()
        player.accept_card(card=new_card)
        hand.append(new_card)
