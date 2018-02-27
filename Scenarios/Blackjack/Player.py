from Scenarios.Blackjack.Card import Card


class Player:
    def wants_new_card(self) -> bool:
        raise NotImplementedError

    def accept_card(self, card: Card):
        raise NotImplementedError
