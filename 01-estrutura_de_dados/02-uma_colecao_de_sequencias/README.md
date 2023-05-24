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

#### Exemplo 01: Criando lista com `for`

```py
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes) # [36, 162, 163, 165, 8364, 164]
```

#### Exemplo 02: Criando lista com compreensão de lista

```py
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes) # [36, 162, 163, 165, 8364, 164]
```

O código do [Exemplo 01](#exemplo-01-criando-lista-com-for) usa o laço _for_, que é ambiguo, pois pode ser utilizado para várias finalidades, como por exemplo calcular a somatória de uma sequência de números. Porém, o [Exemplo 02](#exemplo-02-criando-lista-com-compreensão-de-lista) é mais objetivo, pois a compreensão de listas só possui uma única finalidade: criar uma lista.

Contudo, ao abusar desse recurso, o código pode ficar facilmente ilegível. Assim sendo, use compreensão de lista apenas se for usar a lista gerada ou se o código for curto o suficente para caber em duas linhas.

Compreensões de lista criam listas a partir de sequências ou de qualquer outro tipo iterável, filtrando e transformando os itens.
