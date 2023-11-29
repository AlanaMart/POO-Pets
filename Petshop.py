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
        preco = float(input("Valor: "))
        animal = Animal(codigo, nome, especie, raça, idade, sexo, preco)
        self.animais.append(animal)
        self.salvar()
        print("Animal cadastrado com sucesso.")
        
    def cadastrar_produto(self):
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        produto = Produto(codigo, nome, descricao, preco)
        self.produtos.append(produto)
        self.salvar()
        print("Produto cadastrado com sucesso.")
        
    def cadastrar_servico(self):
        codigo = input("Código do serviço: ")
        nome = input("Nome do serviço: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        servico = Servico(codigo, nome, descricao, preco)
        self.servicos.append(servico)
        self.salvar()
        print("Serviço cadastrado com sucesso.")
        
    def cadastrar_cliente(self):
        codigo = input("Id do cliente: ")
        nome = input("Nome: ")
        telefone = input("telefone: ")
        endereco = input("endereço: ")
        cliente = Cliente(codigo, nome, telefone, endereco)
        self.clientes.append(cliente)
        self.salvar()
        print("Cliente cadastrado com sucesso.")

    def cadastrar_funcionario(self):
        codigo = input("Código do funcionário: ")
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        funcionario = Funcionario(codigo, nome, cargo)
        self.funcionarios.append(funcionario)
        self.salvar()
        print("Funcionario cadastrado com sucesso.")
        
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
                self.salvar()
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
                self.salvar()
                
        elif tipo == "3":
            print("1. Adotar animal")
            print("2. Comprar animal")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                animais_disponiveis_para_adocao = [a for a in self.animais if a.preco == 0]
                if animais_disponiveis_para_adocao:
                    for animal in animais_disponiveis_para_adocao:
                        print(f"{animal.codigo} - {animal.nome} - {animal.especie} - {animal.raça} - {animal.idade} - {animal.sexo}")

                        codigo = input("Código do animal: ")
                        animal = next((a for a in self.animais if a.codigo == codigo), None)
                        if animal:
                            self.animais.remove(animal)
                            print(f"Animal {animal.nome} adotado com sucesso.")
                            self.salvar()
                        else:
                            print("Animal não encontrado.")                    
                else:
                    print("Não há animais disponíveis para adoção.")
                    
            elif escolha == "2":
                animais_disponiveis_compra = [a for a in self.animais if a.preco != 0]
                if animais_disponiveis_compra:
                    for animal in animais_disponiveis_compra:
                        print(f"{animal.codigo} - {animal.nome} - {animal.especie} - {animal.raça} - {animal.idade} - {animal.sexo} - {animal.preco}")
                codigo = input("Código do animal: ")
                quantidade = int(input("Quantidade: "))
                animal = next((a for a in self.animais if a.codigo == codigo), None)
                if animal:
                    self.carrinho.adicionar_item(animal, quantidade)
                    print(f"Animal {animal.nome} adicionado ao carrinho.")
                    self.salvar()
                else:
                    print("Animal não encontrado.")
                   
            else:
                print("Opção Inválida!")
                    
        else:
             print("Opção Inválida!")

    def calcular_total_compra(self):
        return self.carrinho.calcular_total()
    
    def finalizar_compra(self):
    
        codigo_funcionario = input("Digite o código do funcionário: ")
        id_cliente = input("Digite o id do cliente: ")
        funcionario = next((f for f in self.funcionarios if f.codigo == codigo_funcionario), None)
        cliente = next((c for c in self.clientes if c.codigo == id_cliente), None)
        if funcionario and cliente:
            print(f"Recibo de compra")
            print(f"Cliente: {cliente.nome}")
            print(f"Funcionário: {funcionario.nome}")
            print("Itens comprados:")
            for item in self.carrinho.itens:
                print(f"{item['item'].nome}: {item['quantidade']} x {item['item'].preco} = {item['item'].preco * item['quantidade']}")
            print(f"Total da compra: R${self.carrinho.calcular_total():.2f}")
        else:
            print("Funcionário ou cliente não encontrado.")

    


    def salvar(self):
        with open("dados.json", "w") as f:
            json.dump({
                "animais": [animal.to_dict() for animal in self.animais],
                "produtos": [produto.to_dict() for produto in self.produtos],
                "servicos": [servico.to_dict() for servico in self.servicos],
                "clientes": [cliente.to_dict() for cliente in self.clientes],
                "funcionarios": [funcionario.to_dict() for funcionario in self.funcionarios],
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
                #self.carrinho = Carrinho.from_dict(dados["carrinho"])
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
            print("5. Cadastrar Cliente")
            print("6. Cadastrar Funcionario")            
            print("7. Calcular total da compra")
            print("8. Salvar dados")
            print("9. Carregar dados")
            print("0. Sair")
            print("11. finalizar")

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
                self.cadastrar_cliente()
            elif escolha == "6":
                self.cadastrar_funcionario()
            elif escolha == "7":
                print(f"O valor total da compra é de R${self.calcular_total_compra():.2f}")
            elif escolha == "8":
                self.salvar()
            elif escolha == "9":
                self.carregar()
            elif escolha =="11":
                self.finalizar_compra()
            elif escolha == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
                
if __name__ == "__main__":
    sistema = SistemaPetshop()
    sistema.menu()
