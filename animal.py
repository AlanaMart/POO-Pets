
class Animal:
    def __init__(self, codigo, nome, especie, raça, idade, sexo, preco):
        self.codigo = codigo
        self.nome = nome
        self.especie = especie
        self.raça = raça
        self.idade = idade
        self.sexo = sexo
        self.preco = preco

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "especie": self.especie,
            "raça": self.raça,
            "idade": self.idade,
            "sexo": self.sexo,
            "preco": self.preco
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["codigo"], data["nome"], data["especie"], data["raça"], data["idade"], data["sexo"], data["preco"])
    

    
    