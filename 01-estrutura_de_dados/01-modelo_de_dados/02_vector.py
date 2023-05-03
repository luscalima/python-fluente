from math import hypot

# O método hypot retorna a hipotenusa de um triângulo retângulo, ou seja, calcula
# o valor da magnetude do vetor formados pelos valores passados como argumento
# Fórmula da magnetude: |(x, y)| = sqrt(x^2 + y^2)


class Vector:
    # Se ambas coordenadas não forem definidas, o ponto é a origem
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    # Permite que o objeto possa ser representado como a string definida
    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    # Permite chamada com abs
    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    # Permite que o objeto possa ser representado como booleano a partir do valor
    # de verdade de sua magnetude
    def __bool__(self) -> bool:
        return bool(abs(self))

    # Permite operações com + (adição)
    def __add__(self, other: "Vector") -> "Vector":
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Permite operações com * (multiplicação)
    # O código propositalmente só permite multiplicação por escalar
    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)


# Execução

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
v = Vector(3, 4)
print(abs(v))
print(v * 3)
print(abs(v * 3))
