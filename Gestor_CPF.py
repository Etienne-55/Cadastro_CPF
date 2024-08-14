def main():
        is_running = True

        while is_running:
            print("Cadastro de cpf")
            print("1. Cadastrar")
            print("2. Remover")
            print("3. Mostrar lista")
            print("4. exit")

            choice = input("Choose the operation: ")

            if choice == '1':
                adicionar_cpf()

            elif choice == '2':
               remover_cpf() 

            elif choice == '3':
                mostrar_lista()

            elif choice == '4':
                is_running = False

            else:
                print("Opção invalida.")

        print("Operação encerrada.")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome 
        self.cpf = cpf

    def __str__(self):
        return f"nome: {self.nome}, cpf: {self.cpf}"

    def __repr__(self):
        return self.__str__()
pessoa = []

def adicionar_cpf():
    
    nome = input("Informe nome: ")
    cpf = input("Informe CPF: ")

    cliente = Cliente(nome, cpf)
    pessoa.append(cliente)


def mostrar_lista():

    bubble_sort(pessoa)

    if pessoa:
        print("Lista de clientes: ")
        for cliente in pessoa:
            print(cliente)
    else:
        print("Nenhum cliente cadastrado.")


def bubble_sort(pessoa):

    for n in range(len(pessoa) - 1, 0, -1):

        swapped = False

        for i in range(n):
            if pessoa[i].cpf > pessoa[i + 1].cpf:

                swapped = True
                pessoa[i], pessoa[i + 1] = pessoa[i + 1], pessoa[i]

                if not swapped:
                    return

def remover_cpf():
    cpf = input("Informe o CPF do cliente que deseja remover: ")

    for i, Cliente in enumerate(pessoa):
        if Cliente.cpf == cpf:
            del pessoa[i]
            print(f"Cliente com CPF {cpf} removido com sucesso!")
        else:
            print(f"Nenhum cliente com CPF {cpf} encontrado.")


if __name__ == '__main__':
     main()