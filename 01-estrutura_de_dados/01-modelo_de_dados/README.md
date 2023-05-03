# 1 - Modelo de Dados

## 1.1 Um baralho pythônico

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

## 1.2 Como os métodos especiais são usados

Os métodos especiais foram feitos para serem chamados pelo interpretador, e não
diretamente por nosso código, então, mesmo que definamos o `__getitem__` de alguma
classe, o mais adequado é que o invoquemos com a função `len`. A unica exeção para
essa convenção é o método `__init__`, que usamos para trabalhar com inicialização
de classes e super classes.

Outra coisa que podemos fazer com métodos especiais é emular o comportamento numérico
para objetos, como por exemplo, a soma (`+`) de dois objetos da classe `Vector`, que
representa um ponto no espaço de duas dimensões, como mostra o [Exemplo 02](./02_vector.py).

```py
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2 # Vector(4, 5)

# A função abs retora o valor absoluto de números inteiros ou a magnetude de um vetor
v = Vector(3, 4)
abs(v) # 5.0

# Multiplicação por escalar
v * 3 # Vector(9, 12)
abs(v * 3) # 15.0
```

### 1.2.1 Sobre strings

Perceba que no trecho acima, nenhum método especial que foi implementado na classe
é chamado diretamente, pois quem fica a cargo disso no momento é interpretador do Python.

O método especial `__repr__` é definido para se definir uma representação do nosso
objeto como uma string. Por padrão, o console do Python mostraria uma instância de `Vector`
como algo similar a `<Vector object at 0x10e100070>`, mas com o esse método, podemos definir
de forma pouco ou nada (de preferência) ambígua uma string que represente como seria
o código fonte necessário para recriar o objeto que tem esse método invocado. Por
exemplo, uma instância `Vector(1, 2)` seria representada como `"Vector(1, 2)"`. O
interpretador do Python usa o método `repr` para invocar o método `__repr__`.

Caso queiramos definir uma string mais apropriada para o leitura de usuários finais,
usamos o método especial `__str__` que também deve retornar uma string, que é
invocado pelo interpretador do Python pelo método `str`. Se por acaso for julgado que
o retorno de `__repr__` é suficiente, a não implementação de `__str__` resulta na
chamada de `__repr__` pelo método `str`

### 1.2.2 Sobre booleanos

No Python, qualquer objeto pode ser tratado com `True` ou `False`, desde que esteja
inserido em um contexto booleano, ou seja, em um contexto em que valor de verdade
do objeto seja avaliado.

Por padrão, instâncias de classes definidas pelo usuário são avaliadas como `True`.
Contudo, às vezes queremos dar um tratamento diferente baseado nos valores dos atributos
internos da instância.

No nosso exemplo, queremos que um objeto de `Vector` seja avaliado como `False` quando
suas coordenadas forem da orgigem e `True` caso contrário ([linha 25](./02_vector.py#L25)).
Para isso, definimos o método especial `__bool__`, que deve retornar `True` ou `False`
e é invocado pelo interpretador explicitamente com o método `bool` ou implicitamente
quando o objeto está inserido em um contexto booleano.

Para avalição do objeto, primeiro `__bool__` é invocado, caso ele não esteja definido,
`__len__` é invocado. Caso `__len__` esteja definido, se retornar `0` o objeto é avaliado
para `False` e um número diferente resulta em `True`.
