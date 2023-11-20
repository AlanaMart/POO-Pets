import os
import json

from produto import Produto
from animal import Animal
from servico import Servico
from cliente import Cliente
from funcionario import Funcionario
from carrinho import Carrinho

class SistemaPetshop:
    def __init__(self):
        self.animais = []
        self.produtos = []
        self.servicos = []
        self.clientes = []
        self.funcionarios = []
        self.carrinho = Carrinho()
        
    def cadastrar_animal(self):
        codigo = input("Id do animal: ")
        nome = input("Nome do animal: ")
        especie = input("Espécie: ")
        raça = input("Raça: ")
        idade = input("Idade: ")
        sexo = input("Sexo: ")
        preco = input("Valor: ")
        animal = Animal(codigo, nome, especie, raça, idade, sexo, preco)
        self.animais.append(animal)
        print("Animal cadastrado com sucesso.")
        
    def cadastrar_produto(self):
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        produto = Produto(codigo, nome, descricao, preco)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso.")
        
    def cadastrar_servico(self):
        codigo = input("Código do serviço: ")
        nome = input("Nome do serviço: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        servico = Servico(codigo, nome, descricao, preco)
        self.servicos.append(servico)
        print("Serviço cadastrado com sucesso.")
        
    def cadastrar_cliente(self):
        codigo = input("Id do cliente: ")
        nome = input("Nome: ")
        telefone = input("telefone: ")
        endereco = input("endereço: ")
        cliente = Cliente(codigo, nome, telefone, endereco)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")

    def cadastrar_funcionario(self):
        codigo = input("Código do funcionário: ")
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        funcionario = Funcionario(codigo, nome, cargo)
        self.funcionarios.append(funcionario)
        print("Cliente cadastrado com sucesso.")
        
    def adicionar_item_carrinho(self):
        tipo = input("Adicionar:\n1 - produto\n2 - serviço\n3 - animal: ")
        if tipo == "1":
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)
            for produto in dados["produtos"]:
                print(f"{produto['codigo']} - {produto['nome']} - {produto['preco']}")
                
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade: "))
            produto = next((p for p in self.produtos if p.codigo == codigo), None)
            if produto:
                self.carrinho.adicionar_item(produto, quantidade)
                print(f"{quantidade} unidades do produto {produto.nome} adicionadas ao carrinho.")
            else:
                print("Produto não encontrado.")
                
        elif tipo == "2":
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)
            for servico in dados["servicos"]:
                print(f"{servico['codigo']} - {servico['nome']} - {servico['preco']}")
                
            codigo = input("Código do serviço: ")
            quantidade = int(input("Quantidade: "))
            servico = next((s for s in self.servicos if s.codigo == codigo), None)
            if servico:
                self.carrinho.adicionar_item(servico, quantidade)
                print(f"{quantidade} unidades do serviço {servico.nome} adicionadas ao carrinho.")
                
        else:
            print("Opção Inválida!")

    def calcular_total_compra(self):
        return self.carrinho.calcular_total()

    def salvar(self):
        with open("dados.json", "w") as f:
            json.dump({
                "animais": [animal.to_dict() for animal in self.animais],
                "produtos": [produto.to_dict() for produto in self.produtos],
                "servicos": [servico.to_dict() for servico in self.servicos],
                "clientes": [cliente.to_dict() for cliente in self.clientes],
                "funcionarios": [funcionario.to_dict() for funcionario in self.clientes],
                "carrinho": self.carrinho.to_dict(),
            }, f)

    def carregar(self):
        try:
            with open("dados.json", "r") as f:
                dados = json.load(f)
                self.animais = [Animal.from_dict(animal) for animal in dados["animais"]]
                self.produtos = [Produto.from_dict(produto) for produto in dados["produtos"]]
                self.servicos = [Servico.from_dict(servico) for servico in dados["servicos"]]
                self.clientes = [Cliente.from_dict(cliente) for cliente in dados ["clientes"]]
                self.funcionarios = [Funcionario.from_dict(funcionario) for funcionario in dados ["funcionarios"]]
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
