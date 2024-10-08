from cgitb import text
from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto:
    id: Optional[int] = None
    nome: Optional[str]= None
    descricao: Optional[str] = None
    estoque: Optional[str] = None
    preco: Optional[float] = None
    categoria: Optional[text] = None