class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class Lista:
    def __init__(self) :
        self.head = None
        self._size = 0

    def lista_vazia(self) :
        if self._size == 0 :
            return True
        else :
            return False

    def tamanho(self) :
        if lista.lista_vazia() == False:
            return self._size

        return "fila Vazia"

    def adicionar(self ,candidato):
        node = Node (candidato)
        if self.head == None:
            self.head = node

        else:
            ponteiro = self.head
            while ponteiro.next != None :
                ponteiro = ponteiro.next
            ponteiro.next = node
        self._size += 1

    def remove(self):
        if self._size > 0:
            print ("Candidato removido com sucesso. \n")
            self.head = self.head.next

        else :
            print ('fila vazia')

        if self.head is None :
            self.head = None

        self._size -= 1

    def primeiro_candidato(self) :
        if lista.lista_vazia() == True:
            return("Fila Vazia.")

        return str(f"{self.head.data}\n")

    def rodar_lista(self):
        node = Node(str(self.head.data))
        if (self.head == None) :
            self.head = node
        else :
            ponteiro = self.head
            while ponteiro.next != None:
                ponteiro = ponteiro.next
            ponteiro.next = node

        if self._size > 0 :
            self.head = self.head.next

        else :
            print ('fila vazia')

        if self.head is None :
            self.head = None

    def __repr__(self) :
        if self.lista_vazia():
            return 'Fila vazia'
        candidatos = ''
        numero_de_candidatos = self.head
        while(numero_de_candidatos):
            candidatos +=str(numero_de_candidatos.data).capitalize()
            numero_de_candidatos = numero_de_candidatos.next
            if (numero_de_candidatos):
                candidatos += ' '
        return f"{candidatos} \n"

    def rodar_lista_n_vezes(self,num):
        for x in range(num):
            lista.rodar_lista()

    def menu(self):
        resposta = str(input("1- Adicionar candidato\n"
              "2- Mostrar primeiro candidato\n"
              "3- Remover primeiro candidato\n"
              "4- Mostrar todos os candidatos\n"
              "5- Girar a fila dos candidatos\n"
              "6- Girar a fila dos candidatos X vezes\n"))

        lista.opcoes(resposta)

    def opcoes(self,resposta):
        if resposta == "1":
            candidato = str(input("Digite o nome do Candidato: ")).capitalize()
            lista.adicionar(candidato)
            print("Candidato adicionado com sucesso.\n")

        elif resposta == "2":
            print(lista.primeiro_candidato())

        elif resposta == "3":
            lista.remove()

        elif resposta == "4":
            print(lista)

        elif resposta == "5":
            lista.rodar_lista()
            print("Lista girada com sucesso.\n")

        elif resposta == "6":
            resposta = int(input("Digite quantas vezes a fila deve ser girada: "))
            lista.rodar_lista_n_vezes(resposta)
            print(f"A lista foi girada {resposta} vezes com sucesso.\n")

lista = Lista()
while (True):
    lista.menu()
