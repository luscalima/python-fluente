import collections

# O método namedtuple é uma função que permite criar tuplas com campos nomeados.
# É uma classe factory que retorna uma nova classe com um nome (primeiro parâmetro)
# e campos nomeados (segundo parâmentro), onde cada campo pode ser acessado através
# do nome atribuído a ele. É especialmente útil quando se deseja criar uma tupla
# imutável, mas com campos identificáveis por nomes.

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [rank for rank in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # Retorna o tamanho do baralho
    def __len__(self):
        return len(self._cards)
        # return self._cards.__len__()

    def __getitem__(self, position):
        return self._cards[position]
        # return self._cards.__getitem__(position)


# Excução

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[:3])
for card in deck:
    print(card)
print(Card("Q", "hearts") in deck)
