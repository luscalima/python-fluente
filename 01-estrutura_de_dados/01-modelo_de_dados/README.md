# Modelo de Dados

O Modelo de Dados do Python formaliza a interface de elementos que constituem
a própria linguagem. Quando criamos novas classes, a fim de deixá-las no padrão,
usamos métodos especiais para permitir comportamentos básicos. Por exemplo, a
sintaxe `obj[key]` é interpretada como `obj.__getitem__(key)`, onde `__getitem__`
é o método especial.

Usamos métodos especiais quando queremos que nossos objetos possuam comportamentos
fundamentias, como:

- Coleções
- Acesso a atributos
- Iteração
- Sobrecarga de operadores
- Invocação de funções e métodos
- Representação e formatação de strings
- Programação assíncrona
- Criação e destruição de objetos
- Contextos gerenciados

> Métodos como `__getitem__` são chamados de _dunder methods_, pois possuem _double underscore_
> como prefixo e sufixo.

O [Exemplo 01](./01_deck.py) mostra a implementação da `FrenchDeck`, que utiliza
_dunder methods_ para dar suporte ao `len` e acesso por index `[]`.

```py
deck = FrenchDeck()
len(deck) # 52
deck[0] # Card(rank='2', suit='spades')
```

Como a implementação do método `__getitem__` da classe usa o método `__getitem__`
de `_cards`, automaticamente ela oferece suporte ao fatiamento de listas, iteração
em loops e ao operador `in`.

```py
deck[:3]
# [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'),

for card in deck:
    print(card)
# Card(rank='2', suit='spades')
# Card(rank='3', suit='spades')
# Card(rank='4', suit='spades')
# ...

Card('Q', 'hearts') in deck # True
```

Vantagens desse modelo:

- Não é necessário memorizar nome arbitrário para métodos comuns
- Utilização da biblioteca padrão do Python para evitar reinventar a toda

Apesar da `FrenchDeck` herdar implicitamente da classe `object`, a maior parte de
sua funcionalidade não é herdada, isso vem do uso do modelo de dados. Ao implementar
os métodos especiais, a classe `FrenchDeck` se comporta como uma sequência Python padrão,
podendo assim se beneficiar de recursos centrais da linguagem e da biblioteca padrão
