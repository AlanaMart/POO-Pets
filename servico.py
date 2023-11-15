import json
class Serviço:
    def __init__(self, codigo, nome, descricao, preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["codigo"], data["nome"], data["descricao"], data["preco"])
    
