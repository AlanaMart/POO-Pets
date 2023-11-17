class Funcionario:
    def __init__(self, codigo, nome, cargo):
        self.codigo = codigo
        self.nome = nome
        self.cargo = cargo

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "cargo": self.cargo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["codigo"], data["nome"], data["cargo"])