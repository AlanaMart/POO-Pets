
class Animal:
    def __init__(self, nome, especie, raça, idade, sexo):
        self.nome = nome
        self.especie = especie
        self.raça = raça
        self.idade = idade
        self.sexo = sexo

    def to_dict(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "raça": self.raça,
            "idade": self.idade,
            "sexo": self.sexo,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["especie"], data["raça"], data["idade"], data["sexo"])
    

    
    