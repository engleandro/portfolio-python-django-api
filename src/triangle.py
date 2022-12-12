from math import sqrt
from typing import Dict, List, Self, Union 

from src.enumerates import TriangleType
from src.exceptions import EdgeObjectError, VertexDimensionError, VertexObjectError

class Vertex():
    
    def __init__(self, x: Union[float, int], y: Union[float, int]) -> Self:
        self.x = self._check_dimension(x, varname='x')
        self.y = self._check_dimension(y, varname='y')
    
    def _check_dimension(self, dimension: Union[int, float], varname: str="Vertex") -> Union[int, float, Exception]:
        if isinstance(dimension, (float, int)):
            return dimension
        else:
            raise VertexDimensionError(f"{varname} dimension must be a number (integer or float)")
    
    def _check_vertex(self, vertex: Self, name: str="Vertex") -> Union[Self, Exception]:
        if isinstance(vertex, Vertex):
            return vertex
        else:
            raise VertexObjectError(f"{name} must be a VertexObject")
    
    def __str__(self) -> str:
        return f"Vertex({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"VertexObject({self.x}, {self.y})"
    
    def distance_to(self, vertex: Self, decimals: int=2) -> Union[int,float]:
        return round(sqrt((self.x - vertex.x)**2 + (self.y - vertex.y)**2), decimals)
    
    def is_equal_than(self, vertex: Self) -> bool:
        return (self.x == vertex.x) and (self.y == vertex.y)

class Edge(Vertex):
    
    Vertex
    
    def __init__(self, V1: Vertex, V2: Vertex=Vertex(0,0), decimals: int=2) -> Self:
        self.V1 = self._check_vertex(V1, name='V1')
        self.V2 = self._check_vertex(V2, name='V2')
        self.length = self.V1.distance_to(self.V2, decimals=decimals)
    
    def _check_edge(self, edge: Self, name: str="Edge") -> Union[Self, Exception]:
        if isinstance(edge, Edge):
            return edge
        else:
            raise EdgeObjectError(f"{name} must be a EdgeObject")
    
    def __str__(self) -> str:
        return f"Edge({self.V1}, {self.V2})"
    
    def __repr__(self) -> str:
        return f"EdgeObject({self.V1}, {self.V2})"

    def length(self, decimals: int=2) -> Union[float, int]:
        return round(self.V1.distance_to(self.V2), decimals)

class Triangle(Edge, Vertex):
    
    Edge
    
    def __init__(self, V1: Vertex, V2: Vertex, V3: Vertex=Vertex(0,0), accuracy: float=0.01) -> None:
        self.V1 = self._check_vertex(V1, name='V1')
        self.V2 = self._check_vertex(V2, name='V2')
        self.V3 = self._check_vertex(V3, name='V3')
        self.edges = self.set_edges()
        self.perimeter = self.perimeter()
        self.area = self.area()
        self.type = self.type()
    
    def __str__(self) -> str:
        return f"Triangle({self.V1}, {self.V2}, {self.V3})"
    
    def __repr__(self) -> str:
        return f"TriangleObject({self.V1}, {self.V2}, {self.V3})"
    
    def set_edges(self) -> Dict:
        return [
            Edge(self.V1, self.V2),
            Edge(self.V2, self.V3),
            Edge(self.V3, self.V1)
        ]
    
    def lengths(self) -> List[Union[float, int]]:
        self.edges = self.set_edges()
        return [edge.length for edge in self.edges]

    def perimeter(self) -> float:
        self.edges = self.set_edges()
        return sum(self.lengths())
    
    def area(self) -> Union[float, int]:
        self.edges = self.set_edges()
        s = (self.edges[0].length + self.edges[1].length + self.edges[2].length) * 0.5
        return sqrt(s * (s - self.edges[0].length) * (s - self.edges[1].length) * (s - self.edges[2].length))
    
    def is_equilateral(self) -> bool:
        return self.edges[0].length == self.edges[1].length == self.edges[2].length
    
    def is_isoscele(self) -> bool:
        return (self.edges[0].length == self.edges[1].length) \
            or (self.edges[1].length == self.edges[2].length) \
            or (self.edges[2].length == self.edges[0].length)
    
    def is_scalene(self) -> bool:
        return (self.edges[0].length != self.edges[1].length) \
            and (self.edges[1].length != self.edges[2].length) \
            and (self.edges[2].length != self.edges[0].length)

    def type(self) -> str:
        self.edges = self.set_edges()
        if self.is_equilateral():
            return TriangleType.EQUILATERAL
        elif self.is_isosceles():
            return TriangleType.ISOSCELES
        elif self.is_scalene():
            return TriangleType.SCALENE
        else:
            return "unknown"