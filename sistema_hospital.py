class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A/V): ")
        numero = int(input("Digite o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        if not self.head:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f'Cartão {atual.cor} Número {atual.numero}')
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            print(f'Atendendo paciente com cartão {self.head.cor} número {self.head.numero}')
            self.head = self.head.proximo

    def menu(self):
        while True:
            print("1 – Adicionar paciente à fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar paciente")
            print("4 – Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                self.inserir()
            elif opcao == 2:
                self.imprimirListaEspera()
            elif opcao == 3:
                self.atenderPaciente()
            elif opcao == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")

lista_espera = ListaEncadeada()
lista_espera.menu()
