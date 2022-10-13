class Node :
    def __init__(self,data) :
        self.data = data
        self.proximo = None

class Encadeada:
    def __init__(self) :
        self.head = None
        self.tamanho = 0

    def menu(self):
        resposta = str(input("1- Adicionar candidato\n"
              "2- Mostrar primeiro candidato\n"
              "3- Remover primeiro candidato\n"
              "4- Mostrar todos os candidatos\n"
              "5- Girar a fila dos candidatos\n"
              "6- Girar a fila dos candidatos X vezes\n"))

        candidatos_encadeada.opcoes(resposta)

    def opcoes(self,resposta):
        if resposta == "1":
            candidato = str(input("Digite o nome do Candidato: ")).capitalize()
            candidatos_encadeada.adicionar_candidato(candidato)

        elif resposta == "2":
            print(candidatos_encadeada.primeiro_candidato())

        elif resposta == "3":
            print(candidatos_encadeada.remover_candidato())

        elif resposta == "4":
            print(candidatos_encadeada.todos_candidatos())

        elif resposta == "5":
            candidatos_encadeada.rodar_lista()
            if len(candidatos_encadeada) > 0:
                print("Lista girada com sucesso.\n")

        elif resposta == "6":
            if len(candidatos_encadeada) == 0:
                print("Lista Vazia. \n")

            else:
                resposta = int(input("Digite quantas vezes a fila deve ser girada: "))
                candidatos_encadeada.rodar_lista(resposta)
                print(f"A lista foi girada {resposta} vezes com sucesso.\n")


    def __len__(self):
        return self.tamanho

    def adicionar_candidato(self,candidato):
        node = Node(candidato)
        if self.head == None:
            self.head = node

        else:
            ponteiro = self.head
            while ponteiro.proximo != None :
                ponteiro = ponteiro.proximo
            ponteiro.proximo = node
        self.tamanho += 1
        print("Candidato adicionado com sucesso.\n")

    def remover_candidato(self):
        if len(candidatos_encadeada) > 0:
            self.head = self.head.proximo
            self.tamanho -= 1
        else:
            return("fila Vazia. \n")


        if self.head is None:
            self.head = None

        return ("Candidato removido com sucesso. \n")


    def primeiro_candidato(self) :
        if len(candidatos_encadeada) == 0:
            return("Fila Vazia. \n")

        return str(f"{self.head.data}\n")

    def rodar_lista(self,numero_vezes = 1):
        if len(candidatos_encadeada) == 0:
            print("Lista Vazia. \n")

        else:
            for x in range(numero_vezes):
                node = Node(str(self.head.data))
                ponteiro = self.head
                while ponteiro.proximo != None:
                    ponteiro = ponteiro.proximo
                ponteiro.proximo = node
                self.head = self.head.proximo

    def todos_candidatos(self):
        if len(candidatos_encadeada) == 0:
            return 'Fila Vazia. \n'
        candidatos = ''
        numero_de_candidatos = self.head
        while(numero_de_candidatos):
            candidatos +=str(numero_de_candidatos.data).capitalize()
            numero_de_candidatos = numero_de_candidatos.proximo
            if (numero_de_candidatos):
                candidatos += ' '
        return f"{candidatos} \n"

candidatos_encadeada = Encadeada()
while (True):
    candidatos_encadeada.menu()
