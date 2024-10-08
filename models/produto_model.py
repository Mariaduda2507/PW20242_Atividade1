from dataclasses import dataclass
from datetime import date
from numbers import Real
from typing import Optional


@dataclass
class Produto:
    id: Optional[int] = None
    nome: Optional[str]= None
    descricao: Optional[str] = None
    estoque: Optional[str] = None
    preco: Optional[Real] = None
    categoria: Optional[int] = None