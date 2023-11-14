from produto import Produto
import json

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item, quantidade):
        self.itens.append({
            "item": item,
            "quantidade": quantidade,
        })

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item["item"].preco * item["quantidade"]
        return total

    def to_dict(self):
        return {
            "itens": [item["item"].to_dict() for item in self.itens],
            "total": self.calcular_total(),
        }

    @classmethod
    def from_dict(cls, data):
        carrinho = cls()
        carrinho.itens = [{"item": Produto.from_dict(item["item"]), "quantidade": item["quantidade"]} for item in data["itens"]]
        return carrinho
    
