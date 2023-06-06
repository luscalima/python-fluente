# 2 - Uma coleção de sequências

## 2.1 Uma visão geral das sequências _built-in_

Exemplos de sequências da biblioteca padrão do Python:

#### Tabela 03: Exemplos de sequências da biblioteca padrão

| Tipo de Sequência    | Exemplos                             |
| -------------------- | ------------------------------------ |
| Sequências contêiner | `list`, `tuple`, `collections.deque` |
| Sequências planas    | `str`, `bytes`, `array.array`        |

As _sequências contêiner_ guardam referências dos seus valores e as _sequências planas_ propriamente dito e por isso ficam limitadas a valores primitivos (e. g. números e bytes)

#### Tabela 04: Agrupamento por mutabilidade

| Tipo de Sequência    | Exemplos                                                |
| -------------------- | ------------------------------------------------------- |
| Sequências mutáveis  | `list`, `bytearray`, `array.array`, `collections.deque` |
| Sequências imutáveis | `tuple`, `str`, `bytes`                                 |

## 2.2 Compreensão de listas expressões geradoras

Compreensão de lista é um jeito rápido de criar uma sequência (se o alvo é uma `list`) ou uma expressão geradora (para outros tipos de sequências).

### 2.2.1 Compreensão de listas de legibilidade

Quais dos _snippets_ abaixo é mais légivel para a geração de uma lista?

#### Exemplo 03: Criando lista com `for`

```py
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes) # [36, 162, 163, 165, 8364, 164]
```

#### Exemplo 04: Criando lista com compreensão de lista

```py
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes) # [36, 162, 163, 165, 8364, 164]
```

> A função `ord` retorna o valor inteiro que representa o código Unicode de um caractere especificado. Ela é usada para converter um único caractere em seu equivalente numérico. Ela é útil quando é preciso lidar com manipulação de caracteres baseados em seus códigos numéricos.

O código do [Exemplo 03](#exemplo-03-criando-lista-com-for) usa o laço _for_, que é ambiguo, pois pode ser utilizado para várias finalidades, como por exemplo calcular a somatória de uma sequência de números. Porém, o [Exemplo 04](#exemplo-04-criando-lista-com-compreensão-de-lista) é mais objetivo, pois a compreensão de listas só possui uma única finalidade: criar uma lista.

Contudo, ao abusar desse recurso, o código pode ficar facilmente ilegível. Assim sendo, use compreensão de lista apenas se for usar a lista gerada ou se o código for curto o suficente para caber em duas linhas.

Compreensões de lista criam listas a partir de sequências ou de qualquer outro tipo iterável, filtrando e transformando os itens.

## 2.3 Tuplas não são apenas listas imutáveis

Tuplas podem ser usadas de duas formas: (i) como listas imutáveis e (ii) como registros.

### 2.3.1 Tuplas como registros

Tuplas podem conter registros com valores sem campos, onde seus significados são estabelecidos de acordo com a posição em que o valor aparece. Portanto, isso implica que a quantidade de valores é fixada e que sua ordem é importante.

#### Exemplo 05: Tuplas como registro

```py
lax_coordinates = (33.9425, -118.408056) # 1
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014) # 2
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')] # 3
```

1. Latitude e longitude do Aeroporto Internacional de Los Angeles.
1. Dados sobre Tóquio: nome, ano, população (em milhares), crescimento populacional (%) e área (km²).
1. Uma lista de tuplas no formato (código do país, número do passaporte).

Mas muitas vezes não é necessário criar uma classe apenas para nomear os campos. No [Exemplo 5](#exemplo-05-tuplas-como-registro), foi atribuído `('Tokyo', 2003, 32_450, 0.66, 8014)` a `city`, `year`, `pop`, `chg`, `area` em um único comando.

### 2.3.2 Tuplas como listas imutáveis

Existe duas vantagens em usar tuplas (`tuple`) como lista imutáveis:

- **Clareza**: imediatamente é sabido que uma `tuple` no código nunca mudará de tamanho.
- **Desempenho**: uma `tuple` é mais perfomática que uma `list`.

> **Importante**: a imutabilidade de uma `tuple` só se aplica a suas referências diretas, ou seja, caso uma referência aponte para um outro objeto mutável, e esse tenha seu valor alterado, o valor da `tuple` mudará, porém aquela referência nunca poderá ser apagada ou modificada.

Uma `tuple` com valores mutáveis pode ser fonte de _bugs_, caso seja usada como chave de um dicionário (`dict`) ou valor de um conjunto (`set`), por exemplo, já que seu valor é volátil. Para definir explicitamente se um `tuple` é volátil ou não, em termos de valor, é possível usar a função _built-in_ `hash`.

```py
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
fixed(tf) # True
fixed(tm) # False
```

> **Sobre `hash`**: A função `hash` é usada para calcular o valor hash de um objeto. O valor _hash_ é um número inteiro que é usado para identificar exclusivamente o objeto durante uma sessão de execução do programa. Essa função aceita um único argumento, que pode ser um objeto de qualquer tipo imutável. Objetos com valores mutáveis, como listas e dicionários, não podem ser usados como argumentos.

Apesar dessa resalva, abaixo é mostrado algumas vantagens em usar `tuple` como `list` imutável.

- Para avaliar uma `tuple`, o interpretador Python gera _bytecode_ para uma constante, mas para uma `list`, o _bytecode_ gerado insere cada elemento como uma constante separada no _stack_ de dados, e então cria a lista.
- Dada uma `tuple` `t`, `tuple(t)` devolve uma referência para a mesma `t`. Não há necessidade de cópia. Por outro lado, dada uma `list` `l`, o construtor `list(l)` precisa criar uma nova cópia de `l`.
- Devido a seu tamanho fixo, uma instância de `tuple` tem alocado para si o espaço exato de memória que precisa. Já uma instância de `list` tem memória adicional alocada, para amortizar o custo de acréscimos futuros.
