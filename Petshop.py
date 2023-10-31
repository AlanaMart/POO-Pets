import os
import json

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

class Produto:
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

class SistemaPetshop:
    def __init__(self):
        self.animais = []
        self.produtos = []
        self.servicos = []
        self.carrinho = Carrinho()

    def cadastrar_animal(self):
        nome = input("Nome do animal: ")
        especie = input("Espécie: ")
        raça = input("Raça: ")
        idade = input("Idade: ")
        sexo = input("Sexo: ")
        animal = Animal(nome, especie, raça, idade, sexo)
        self.animais.append(animal)
        print("Animal cadastrado com sucesso.")

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        produto = Produto(nome, descricao, preco)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso.")

    def cadastrar_servico(self):
        nome = input("Nome do serviço: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        servico = Serviço(nome, descricao, preco)
        self.servicos.append(servico)
        print("Serviço cadastrado com sucesso.")

    def adicionar_item_carrinho(self):
        tipo = input("Tipo (produto/serviço): ")
        if tipo == "produto":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            produto = next((p for p in self.produtos if p.nome == nome), None)
            if produto:
                self.carrinho.adicionar_item(produto, quantidade)
                print(f"{quantidade} unidades do produto {nome} adicionadas ao carrinho.")
            else:
                print("Produto não encontrado.")
        elif tipo == "serviço":
            nome = input("Nome do serviço: ")
            quantidade = int(input("Quantidade: "))
            servico = next((s for s in self.servicos if s.nome == nome), None)
            if servico:
                self.carrinho.adicionar_item(servico, quantidade)
                print(f"{quantidade} unidades do serviço {nome} adicionadas ao carrinho.")
            else:
                print("Serviço não encontrado.")
        else:
            print("Tipo inválido. Use 'produto' ou 'serviço'.")

    def calcular_total_compra(self):
        return self.carrinho.calcular_total()

    def salvar(self):
        with open("dados.json", "w") as f:
            json.dump({
                "animais": [animal.to_dict() for animal in self.animais],
                "produtos": [produto.to_dict() for produto in self.produtos],
                "servicos": [servico.to_dict() for servico in self.servicos],
                "carrinho": self.carrinho.to_dict(),
            }, f)

    def carregar(self):
        try:
            with open("dados.json", "r") as f:
                dados = json.load(f)
                self.animais = [Animal.from_dict(animal) for animal in dados["animais"]]
                self.produtos = [Produto.from_dict(produto) for produto in dados["produtos"]]
                self.servicos = [Serviço.from_dict(servico) for servico in dados["servicos"]]
                self.carrinho = Carrinho.from_dict(dados["carrinho"])
                print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo 'dados.json' não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao carregar os dados do arquivo JSON.")

    def menu(self):
        while True:
            print("1. Cadastrar animal")
            print("2. Cadastrar produto")
            print("3. Cadastrar serviço")
            print("4. Adicionar item ao carrinho")
            print("5. Calcular total da compra")
            print("6. Salvar dados")
            print("7. Carregar dados")
            print("8. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.cadastrar_animal()
            elif escolha == "2":
                self.cadastrar_produto()
            elif escolha == "3":
                self.cadastrar_servico()
            elif escolha == "4":
                self.adicionar_item_carrinho()
            elif escolha == "5":
                print(f"O valor total da compra é de R${self.calcular_total_compra():.2f}")
            elif escolha == "6":
                self.salvar()
            elif escolha == "7":
                self.carregar()
            elif escolha == "8":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaPetshop()
    sistema.menu()
