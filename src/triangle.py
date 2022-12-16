from math import sqrt
from typing import Dict, List, Self, Union

from src.enumerates import TriangleType
from src.exceptions import EdgeObjectError, VertexDimensionError, VertexObjectError


class Vertex:
    def __init__(self, x: Union[float, int], y: Union[float, int]) -> Self:
        self.x = self._check_dimension(x, varname="x")
        self.y = self._check_dimension(y, varname="y")

    def _check_dimension(
        self, dimension: Union[int, float], varname: str = "Vertex"
    ) -> Union[int, float, Exception]:
        if isinstance(dimension, (float, int)):
            return dimension
        else:
            raise VertexDimensionError(
                f"{varname} dimension must be a number (integer or float)"
            )

    def _check_vertex(
        self, vertex: Self, name: str = "Vertex"
    ) -> Union[Self, Exception]:
        if isinstance(vertex, Vertex):
            return vertex
        else:
            raise VertexObjectError(f"{name} must be a VertexObject")

    def __str__(self) -> str:
        return f"Vertex({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"VertexObject({self.x}, {self.y})"

    def distance_to(self, vertex: Self, decimals: int = 2) -> Union[int, float]:
        return round(
            sqrt((self.x - vertex.x) ** 2 + (self.y - vertex.y) ** 2), decimals
        )

    def is_equal_than(self, vertex: Self) -> bool:
        return (self.x == vertex.x) and (self.y == vertex.y)


class Edge(Vertex):

    Vertex

    def __init__(
        self, V1: Vertex, V2: Vertex = Vertex(0, 0), decimals: int = 2
    ) -> Self:
        self.V1 = self._check_vertex(V1, name="V1")
        self.V2 = self._check_vertex(V2, name="V2")
        self.length = self.V1.distance_to(self.V2, decimals=decimals)

    def _check_edge(self, edge: Self, name: str = "Edge") -> Union[Self, Exception]:
        if isinstance(edge, Edge):
            return edge
        else:
            raise EdgeObjectError(f"{name} must be a EdgeObject")

    def __str__(self) -> str:
        return f"Edge({self.V1}, {self.V2})"

    def __repr__(self) -> str:
        return f"EdgeObject({self.V1}, {self.V2})"

    def length(self, decimals: int = 2) -> Union[float, int]:
        return round(self.V1.distance_to(self.V2), decimals)


class Triangle(Edge, Vertex):

    Edge

    def __init__(
        self,
        V1: Vertex = Vertex(0, 0),
        V2: Vertex = Vertex(0, 0),
        V3: Vertex = Vertex(0, 0),
    ) -> None:
        self.V1 = self._check_vertex(V1, name="V1")
        self.V2 = self._check_vertex(V2, name="V2")
        self.V3 = self._check_vertex(V3, name="V3")

    def __str__(self) -> str:
        return f"Triangle({self.V1}, {self.V2}, {self.V3})"

    def __repr__(self) -> str:
        return f"TriangleObject({self.V1}, {self.V2}, {self.V3})"

    def set_edges(self) -> Dict:
        return [Edge(self.V1, self.V2), Edge(self.V2, self.V3), Edge(self.V3, self.V1)]

    def lengths(self) -> List[Union[float, int]]:
        self.edges = self.set_edges()
        return [edge.length for edge in self.edges]

    def _check_triangle_by_lengths(self, lengths: List[Union[str, int]]) -> bool:
        if not lengths:
            lengths = self.lengths()
        lengths_to_check, hipotenuse = lengths.copy(), max(lengths)
        lengths_to_check.remove(hipotenuse)
        return sum(lengths_to_check) > hipotenuse

    def _check_lengths(
        self, lengths: List[Union[str, int]]
    ) -> List[Union[str, int, Exception]]:
        if (
            len(lengths) == 3
            and all([isinstance(length, (int, float)) for length in lengths])
            and all([True if length > 0 else False for length in lengths])
            and self._check_triangle_by_lengths(lengths)
        ):
            return lengths
        else:
            raise ValueError(
                "Lengths must be a list of three numbers (int, float) greater "
                "than zero and the sum of the lengths of any two sides must be "
                "greater than or equal to the length of the third side."
            )

    def hipotenuse(self) -> Union[float, int]:
        lengths = self.lengths()
        return max(lengths)

    def perimeter(self) -> float:
        self.edges = self.set_edges()
        return sum(self.lengths())

    def area(self) -> Union[float, int]:
        self.edges = self.set_edges()
        s = (self.edges[0].length + self.edges[1].length + self.edges[2].length) * 0.5
        return sqrt(
            s
            * (s - self.edges[0].length)
            * (s - self.edges[1].length)
            * (s - self.edges[2].length)
        )

    def is_equilateral(self, lengths: List[Union[str, int]] = []) -> bool:
        if not lengths:
            lengths = self.lengths()
        lengths = self._check_lengths(lengths)
        return lengths[0] == lengths[1] == lengths[2]

    def is_isosceles(self, lengths: List[Union[str, int]] = []) -> bool:
        if not lengths:
            lengths = self.lengths()
        lengths = self._check_lengths(lengths)
        return (
            (lengths[0] == lengths[1])
            or (lengths[1] == lengths[2])
            or (lengths[2] == lengths[0])
        )

    def is_scalene(self, lengths: List[Union[str, int]] = []) -> bool:
        if not lengths:
            lengths = self.lengths()
        lengths = self._check_lengths(lengths)
        return (
            (lengths[0] != lengths[1])
            and (lengths[1] != lengths[2])
            and (lengths[2] != lengths[0])
        )

    def type(self, lengths: List[Union[int, float]] = []) -> str:
        if not lengths:
            lengths = self.lengths()
        lengths = self._check_lengths(lengths=lengths)
        if self.is_equilateral(lengths=lengths):
            return TriangleType.EQUILATERAL
        elif self.is_isosceles(lengths=lengths):
            return TriangleType.ISOSCELES
        elif self.is_scalene(lengths=lengths):
            return TriangleType.SCALENE
        else:
            return "unknown"
