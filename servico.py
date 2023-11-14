import json
class Serviço:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["descricao"], data["preco"])
    
