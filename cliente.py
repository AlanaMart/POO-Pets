class Cliente:
    def __init__(self, codigo, nome, telefone, endereco):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.endereco =endereco

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["codigo"], data["nome"], data["telefone"], data["endereco"])